from __future__ import annotations

import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

import config
from rag.src.llm.prompts import build_doc_prompt
from rag.src.llm.qwen import generate
from rag.src.retrieval.doc_retriever import DocRetriever
from rag.src.retrieval.reranker import rerank
from shared.types import Question
from shared.utils.logger import get_logger

logger = get_logger("doc_pipeline", config.LOGS_DIR)

_retriever: DocRetriever | None = None

_ANSWER_RE = re.compile(r"\b([A-D]{1,4})\b")


def _get_retriever() -> DocRetriever:
    global _retriever
    if _retriever is None:
        _retriever = DocRetriever()
    return _retriever


def _parse_note(note: str) -> dict[str, str]:
    """Parse note field "A, Đáp án A\n B, Đáp án B\n..." → {"A": "Đáp án A", ...}"""
    options: dict[str, str] = {}
    for line in note.strip().split("\n"):
        line = line.strip()
        if line and "," in line:
            key, val = line.split(",", 1)
            k = key.strip().upper()
            if k in {"A", "B", "C", "D"}:
                options[k] = val.strip()
    return options


def _extract_answer(raw: str) -> str:
    """Extract đáp án từ raw LLM output. Trả về chuỗi chữ cái, vd 'A', 'AB'."""
    # Tìm pattern "Đáp án: X" hoặc "Answer: X" hoặc chữ cái cuối câu
    # Ưu tiên pattern ở cuối output
    lines = [l.strip() for l in raw.strip().split("\n") if l.strip()]
    for line in reversed(lines):
        m = _ANSWER_RE.search(line)
        if m:
            return m.group(1)
    # fallback: lấy match đầu tiên trong toàn bộ output
    m = _ANSWER_RE.search(raw)
    return m.group(1) if m else "A"


def run(question: Question) -> dict:
    """Chạy call_document pipeline cho 1 câu hỏi MCQ.

    Returns:
        dict: {id, function_code, function_result, time_response}
        function_result là chuỗi chữ cái đáp án, vd "A" hoặc "AB"
    """
    t_start = time.perf_counter()
    retriever = _get_retriever()

    doc_id = DocRetriever.extract_doc_id(question.question) if config.DOC_USE_FILTER else None
    chunks = retriever.search(question.question, top_k=20, doc_id=doc_id)

    top_chunks = rerank(question.question, chunks, top_k=config.RERANK_TOP_K)
    if not top_chunks and chunks:
        top_chunks = chunks[:config.RERANK_TOP_K]

    options = _parse_note(question.note or "")
    prompt = build_doc_prompt(top_chunks, question.question, options)

    t0 = time.perf_counter()
    raw_output = generate(prompt)
    answer = _extract_answer(raw_output)
    ms_llm = round((time.perf_counter() - t0) * 1000)
    logger.info("stage_llm", extra={"id": question.id, "answer": answer, "ms": ms_llm})
    print(f"[doc] id={question.id}  llm={ms_llm}ms  answer={answer}")

    time_response = round(time.perf_counter() - t_start, 3)
    return {
        "id": question.id,
        "function_code": "call_document",
        "function_result": answer,
        "time_response": time_response,
    }
