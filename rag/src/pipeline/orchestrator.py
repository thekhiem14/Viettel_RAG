from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from intent.src.classifier import predict
from rag.src.pipeline import api_pipeline, doc_pipeline
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
        print(f"[warmup] {name}: {time.perf_counter() - t:.2f}s")

    # 1. Embedder (bge-m3) — dùng chung classifier + doc + api retrievers
    def _w_embedder() -> None:
        from rag.src.indexing.embedder import Embedder
        Embedder().encode_query("warmup")
    _stage("Embedder", _w_embedder)

    # 2. APIRetriever + DocRetriever (load FAISS/BM25/Fuzzy + dummy search)
    def _w_retrievers() -> None:
        from rag.src.retrieval.api_retriever import APIRetriever
        from rag.src.retrieval.doc_retriever import DocRetriever
        APIRetriever().search("warmup")
        DocRetriever().search("warmup", top_k=5)
    _stage("Retrievers (API + Doc)", _w_retrievers)

    # 3. Reranker (bge-reranker-v2-m3) — chỉ doc pipeline dùng
    def _w_reranker() -> None:
        from rag.src.retrieval.reranker import rerank
        from shared.types import Chunk
        dummy = Chunk(chunk_id="_w", doc_id="_w", heading_path="_", level=0, char_count=5, text="dummy")
        rerank("warmup", [dummy], top_k=1)
    _stage("Reranker", _w_reranker)

    # 4. LLM (Qwen3-4B 4-bit) — chậm nhất, ~10-30s lần đầu
    def _w_llm() -> None:
        from rag.src.llm.qwen import generate
        generate("Trả lời 'A':")
    _stage("LLM (Qwen3-4B)", _w_llm)

    # 5. Intent classifier — wrapper quanh Embedder + FaissStore (đã warm ở #1+#2)
    def _w_intent() -> None:
        predict(Question(id=0, question="warmup", note=None))
    _stage("Intent classifier", _w_intent)


def run_one(question: Question) -> dict:
    """Route 1 câu hỏi → đúng pipeline → output dict."""
    label, confidence = predict(question)
    logger.info("intent", extra={"id": question.id, "label": label, "confidence": confidence})

    try:
        if label == "call_document":
            return doc_pipeline.run(question)
        else:
            return api_pipeline.run(question)
    except Exception as e:
        logger.error("pipeline_error", extra={"id": question.id, "error": str(e)})
        return {
            "id": question.id,
            "function_code": label,
            "function_result": "",
            "time_response": 0.0,
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
