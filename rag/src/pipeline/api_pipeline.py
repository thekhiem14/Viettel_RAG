from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

import config
from rag.src.llm.json_validator import validate_api_output
from rag.src.llm.prompts import build_api_prompt
from rag.src.llm.qwen import generate
from rag.src.retrieval.api_retriever import APIRetriever
from shared.types import APIEntry, Question

_retriever: APIRetriever | None = None
_schemas: dict[str, APIEntry] | None = None


def _get_retriever() -> APIRetriever:
    global _retriever
    if _retriever is None:
        _retriever = APIRetriever()
    return _retriever


def _get_schemas() -> dict[str, APIEntry]:
    global _schemas
    if _schemas is None:
        raw = json.loads(config.API_SCHEMAS.read_text(encoding="utf-8"))
        _schemas = {fc: APIEntry(**entry) for fc, entry in raw.items()}
    return _schemas


def run(question: Question) -> dict:
    """Chạy call_api pipeline cho 1 câu hỏi.

    Returns:
        dict: {id, function_code, function_result, time_response}
        function_result là JSON string: {"func_code": ..., "path": ..., "body": {...}}
    """
    t_start = time.perf_counter()

    retriever = _get_retriever()
    schemas = _get_schemas()

    hits = retriever.search(question.question)

    candidates: list[APIEntry] = []
    for hit in hits:
        if hit.id in schemas:
            candidates.append(schemas[hit.id])

    if not candidates:
        # fallback nếu retriever trả về kết quả không có trong schemas
        candidates = list(schemas.values())[:config.API_RETRIEVE_TOP_K]

    prompt = build_api_prompt(question.question, candidates)
    raw_output = generate(prompt)

    result = validate_api_output(raw_output, candidates)

    time_response = round(time.perf_counter() - t_start, 3)

    return {
        "id": question.id,
        "function_code": "call_api",
        "function_result": json.dumps(result, ensure_ascii=False),
        "time_response": time_response,
    }
