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
from shared.utils.logger import get_logger

logger = get_logger("api_pipeline", config.LOGS_DIR)

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

    t0 = time.perf_counter()
    hits = retriever.search(question.question)
    candidates: list[APIEntry] = [schemas[h.id] for h in hits if h.id in schemas]
    if not candidates:
        candidates = list(schemas.values())[:config.API_RETRIEVE_TOP_K]
    ms_ret = round((time.perf_counter() - t0) * 1000)
    top1 = candidates[0].func_code if candidates else ""
    logger.info("stage_retrieval", extra={"id": question.id, "n_candidates": len(candidates), "top1": top1, "ms": ms_ret})
    print(f"[api] id={question.id}  retrieval={ms_ret}ms  candidates={len(candidates)}  top1={top1}")

    if config.SKIP_LLM:
        result = {"func_code": candidates[0].func_code, "path": candidates[0].path, "body": {}}
        logger.info("stage_llm_skipped", extra={"id": question.id, "func_code": result["func_code"]})
        print(f"[api] id={question.id}  llm=SKIPPED  func_code={result['func_code']}")
    else:
        t0 = time.perf_counter()
        prompt = build_api_prompt(question.question, candidates)
        raw_output = generate(prompt)
        result = validate_api_output(raw_output, candidates)
        ms_llm = round((time.perf_counter() - t0) * 1000)
        logger.info("stage_llm", extra={"id": question.id, "func_code": result.get("func_code"), "ms": ms_llm})
        print(f"[api] id={question.id}  llm={ms_llm}ms  func_code={result.get('func_code')}")

    time_response = round(time.perf_counter() - t_start, 3)
    print(f"[api] id={question.id}  TOTAL={time_response:.2f}s")
    return {
        "id": question.id,
        "function_code": "call_api",
        "function_result": json.dumps(result, ensure_ascii=False),
        "time_response": time_response,
    }
