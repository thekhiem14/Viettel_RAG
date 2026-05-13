from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

import config
from rag.src.llm.json_validator import validate_body_output
from rag.src.llm.prompts import build_api_prompt, _load_aliases
from rag.src.llm.qwen import generate
from rag.src.retrieval.api_retriever import APIRetriever
from shared.types import APIEntry, Question
from shared.utils.logger import get_logger

logger = get_logger("api_pipeline", config.LOGS_DIR)

_retriever: APIRetriever | None = None
_schemas: dict[str, APIEntry] | None = None

# Params cần lookup từ aliases thay vì để LLM đoán
_LOOKUP_PARAMS = {"projectId", "projectList", "customerList"}


def _prefill_from_aliases(question: str, candidate: APIEntry) -> dict:
    """Scan câu hỏi để tìm project/customer names và map sang API values.

    Chỉ xử lý params thuộc _LOOKUP_PARAMS có trong required+optional của candidate.
    Trả về dict các key đã được pre-fill (có thể rỗng nếu không match).
    """
    aliases = _load_aliases()
    all_params = candidate.required_params + candidate.optional_params
    param_names = {p["name"] for p in all_params if "name" in p}
    prefill: dict = {}

    for param in _LOOKUP_PARAMS & param_names:
        entries = aliases.get(param, [])
        matched = []
        for entry in entries:
            key = str(entry.get("key", ""))
            if key and key in question:
                matched.append(entry["value"])
        if matched:
            # projectId là scalar (lấy first), projectList/customerList là list
            if param == "projectId":
                prefill[param] = matched[0]
            else:
                prefill[param] = matched
    return prefill


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

    top1 = candidates[0]
    prefill = _prefill_from_aliases(question.question, top1)
    if config.SKIP_LLM:
        body = top1.example_body or {}
        logger.info("stage_llm_skipped", extra={"id": question.id, "func_code": top1.func_code})
        print(f"[api] id={question.id}  llm=SKIPPED  func_code={top1.func_code}")
    else:
        t0 = time.perf_counter()
        prompt = build_api_prompt(question.question, top1)
        raw_output = generate(prompt)
        body = validate_body_output(raw_output)
        valid_keys = {p["name"] for p in top1.required_params + top1.optional_params if "name" in p}
        body = {k: v for k, v in body.items() if k in valid_keys}
        # prefill overrides LLM output cho project/customer params
        body.update(prefill)
        ms_llm = round((time.perf_counter() - t0) * 1000)
        logger.info("stage_llm", extra={"id": question.id, "func_code": top1.func_code, "ms": ms_llm})
        print(f"[api] id={question.id}  llm={ms_llm}ms  func_code={top1.func_code}")
    result = {"func_code": top1.func_code, "path": top1.path, "body": body}

    time_response = round(time.perf_counter() - t_start, 3)
    print(f"[api] id={question.id}  body={result.get('body')}")
    print(f"[api] id={question.id}  TOTAL={time_response:.2f}s")
    return {
        "id": question.id,
        "function_code": "call_api",
        "function_result": json.dumps(result, ensure_ascii=False),
        "time_response": time_response,
    }
