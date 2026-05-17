from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from intent.src.classifier import predict
from rag.src.pipeline import api_pipeline, api_pipeline_v2, doc_pipeline
from shared.types import Question
from shared.utils.logger import get_logger

import config

logger = get_logger("orchestrator", config.LOGS_DIR)


def warmup() -> None:
    """Force load + chạy dummy 1 lần cho mỗi component.

    Gọi TRƯỚC khi đọc file test để time_response không bị tính cold-start.
    Tổng thời gian warm-up ~30-60s là bình thường (chỉ 1 lần).
    """
    def _stage(name: str, fn) -> None:
        t = time.perf_counter()
        fn()
        elapsed = time.perf_counter() - t
        print(f"[warmup] {name}: {elapsed:.2f}s")

    print("[warmup] Starting...")
    t_total = time.perf_counter()

    # 1. Embedder (bge-m3) — dùng chung classifier + doc + api retrievers
    def _w_embedder() -> None:
        from rag.src.indexing.embedder import Embedder
        print(f"  [1a] Importing + init Embedder... ", end="", flush=True)
        t = time.perf_counter()
        Embedder().encode_query("warmup")
        print(f"{time.perf_counter() - t:.2f}s")
    _stage("1. Embedder (bge-m3)", _w_embedder)

    # 2. APIRetriever + DocRetriever (load FAISS/BM25/Fuzzy + dummy search)
    def _w_retrievers() -> None:
        from rag.src.retrieval.api_retriever import APIRetriever
        from rag.src.retrieval.doc_retriever import DocRetriever
        print(f"  [2a] APIRetriever.search()... ", end="", flush=True)
        t = time.perf_counter()
        APIRetriever().search("warmup")
        print(f"{time.perf_counter() - t:.2f}s")
        print(f"  [2b] DocRetriever.search()... ", end="", flush=True)
        t = time.perf_counter()
        DocRetriever().search("warmup", top_k=5)
        print(f"{time.perf_counter() - t:.2f}s")
    _stage("2. Retrievers (FAISS+BM25+Fuzzy)", _w_retrievers)

    # 3. Reranker (bge-reranker-v2-m3) — chỉ doc pipeline dùng
    def _w_reranker() -> None:
        from rag.src.retrieval.reranker import rerank
        from shared.types import Chunk
        print(f"  [3a] rerank() + load model... ", end="", flush=True)
        t = time.perf_counter()
        dummy = Chunk(chunk_id="_w", doc_id="_w", heading_path="_", level=0, char_count=5, text="dummy")
        rerank("warmup", [dummy], top_k=1)
        print(f"{time.perf_counter() - t:.2f}s")
    _stage("3. Reranker (bge-reranker-v2-m3)", _w_reranker)

    # 4. LLM (2.5-3B 4-bit) — chậm nhất, ~10-30s lần đầu
    def _w_llm() -> None:
        from rag.src.llm.qwen import generate
        print(f"  [4a] generate() load model + tokenizer... ", end="", flush=True)
        t = time.perf_counter()
        output = generate("Trả lời 'A':")
        print(f"{time.perf_counter() - t:.2f}s (output: {len(output)} chars)")
    _stage("4. LLM (Qwen2.5-3B 4-bit)", _w_llm)

    # 5. Intent classifier — wrapper quanh Embedder + FaissStore (đã warm ở #1+#2)
    def _w_intent() -> None:
        print(f"  [5a] predict() inference... ", end="", flush=True)
        t = time.perf_counter()
        label, conf = predict(Question(id=0, question="warmup", note=None))
        print(f"{time.perf_counter() - t:.2f}s (label={label}, conf={conf:.3f})")
    _stage("5. Intent classifier", _w_intent)

    total_elapsed = time.perf_counter() - t_total
    print(f"\n[warmup] DONE in {total_elapsed:.1f}s (ready for inference)\n")


def run_one(question: Question) -> dict:
    """Route 1 câu hỏi → đúng pipeline → output dict."""
    t_start = time.perf_counter()
    label, confidence = predict(question)
    logger.info("intent", extra={"id": question.id, "label": label, "confidence": confidence})

    try:
        if label == "call_document":
            result = doc_pipeline.run(question)
        else:
            if getattr(config, "USE_API_V2", False):
                result = api_pipeline_v2.run(question)
            else:
                result = api_pipeline.run(question)
        result["time_response"] = round(time.perf_counter() - t_start, 3)
        return result
    except Exception as e:
        logger.error("pipeline_error", extra={"id": question.id, "error": str(e)})
        fallback = "A" if label == "call_document" else ""
        return {
            "id": question.id,
            "function_code": label,
            "function_result": fallback,
            "raw_llm": "",
            "time_response": round(time.perf_counter() - t_start, 3),
        }


def run_batch(questions: list[Question]) -> list[dict]:
    """Chạy tuần tự, log từng câu. Dùng cho eval + inference."""
    results = []
    for i, q in enumerate(questions):
        result = run_one(q)
        results.append(result)
        if (i + 1) % 10 == 0:
            logger.info("batch_progress", extra={"done": i + 1, "total": len(questions)})
    return results

if __name__ == "__main__":
    warmup()