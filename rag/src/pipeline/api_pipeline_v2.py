from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

import config
from rag.src.extract.param_extractor import extract_all
from rag.src.llm.json_validator import validate_body_output
from rag.src.llm.prompts_v2 import build_api_prompt_v2
from rag.src.llm.qwen import generate
from rag.src.retrieval.api_retriever import APIRetriever
from shared.types import APIEntry, Question
from shared.utils.logger import get_logger

logger = get_logger("api_pipeline_v2", config.LOGS_DIR)

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


def _default_for_type(type_str: str):
    t = (type_str or "").lower()
    if "list" in t:
        return []
    if "bool" in t:
        return None
    if "date" in t:
        return ""
    if "int" in t or "long" in t:
        return None
    if "string" in t:
        return ""
    return None


def _build_fallback_body(candidate: APIEntry, pre_filled: dict) -> dict:
    """Fallback khi LLM fail: dùng example_body + pre_filled, đảm bảo đủ key."""
    required = candidate.required_params or []
    optional = candidate.optional_params or []
    schema_params = {p["name"]: p for p in required + optional if "name" in p}
    valid_keys = set(schema_params.keys())

    body: dict = {}
    # Bắt đầu từ example_body
    if candidate.example_body and isinstance(candidate.example_body, dict):
        for k, v in candidate.example_body.items():
            if k in valid_keys:
                body[k] = v
    # Fill key còn thiếu bằng default
    for k, p in schema_params.items():
        if k not in body:
            body[k] = _default_for_type(p.get("type", ""))
    # Override bằng pre_filled (rule-based đã chắc chắn)
    for k, v in pre_filled.items():
        if k in valid_keys:
            body[k] = v
    return body


def _coerce_and_order(body: dict, candidate: APIEntry) -> dict:
    """Ép kiểu + đảm bảo null/[] không bị drop + sort key theo schema order."""
    required = candidate.required_params or []
    optional = candidate.optional_params or []
    schema_params = {p["name"]: p for p in required + optional if "name" in p}
    valid_keys = set(schema_params.keys())

    coerced: dict = {}
    for k, p in schema_params.items():
        v = body.get(k)  # lấy từ body LLM, có thể None/missing
        ptype = (p.get("type") or "").lower()

        if "list" in ptype:
            # null/missing → [], string → [string]
            if v is None:
                v = []
            elif isinstance(v, str):
                v = [v] if v else []
            elif not isinstance(v, list):
                v = [v]
        elif "bool" in ptype:
            if isinstance(v, str):
                v = {"true": True, "false": False}.get(v.lower(), None)
        elif "int" in ptype or "long" in ptype:
            if isinstance(v, str):
                v = int(v) if v.lstrip("-").isdigit() else None
        elif "date" in ptype:
            if not isinstance(v, str):
                v = ""

        # Giữ key dù null/[] — KHÔNG drop
        if k in valid_keys:
            coerced[k] = v

    # Thứ tự: required trước, optional sau (theo thứ tự schema)
    order = [p["name"] for p in required + optional if "name" in p]
    return {k: coerced[k] for k in order if k in coerced}


def run(question: Question) -> dict:
    """call_api pipeline v2.

    Flow:
      S1. Retrieval → top-1 API
      S2. Rule-based extract → pre_filled (chỉ date + organization + projectList)
      S3. LLM fill full body (đọc description, override pre_filled cuối cùng)
      S4. Coerce + order (đảm bảo null/[] giữ nguyên, đúng kiểu)
    """
    t_start = time.perf_counter()
    retriever = _get_retriever()
    schemas = _get_schemas()

    # S1: Retrieval
    t0 = time.perf_counter()
    hits = retriever.search(question.question)
    candidates: list[APIEntry] = [schemas[h.id] for h in hits if h.id in schemas]
    if not candidates:
        candidates = list(schemas.values())[:config.API_RETRIEVE_TOP_K]
    ms_ret = round((time.perf_counter() - t0) * 1000)
    top1 = candidates[0]
    logger.info("stage_retrieval", extra={"id": question.id, "top1": top1.func_code, "ms": ms_ret})
    print(f"[api_v2] id={question.id}  retrieval={ms_ret}ms  top1={top1.func_code}")

    # S2: Rule-based extract (date, organization, projectList)
    t0 = time.perf_counter()
    pre_filled = extract_all(question.question)
    ms_ext = round((time.perf_counter() - t0) * 1000)
    print(f"[api_v2] id={question.id}  extract={ms_ext}ms  pre_filled={list(pre_filled.keys())}")

    # S3: LLM fill full body
    raw_llm = ""
    if config.SKIP_LLM:
        body = _build_fallback_body(top1, pre_filled)
        print(f"[api_v2] id={question.id}  llm=SKIPPED (SKIP_LLM)")
    else:
        t0 = time.perf_counter()
        prompt = build_api_prompt_v2(question.question, top1, pre_filled)
        llm_ok = False
        for attempt in range(2):
            try:
                raw = generate(prompt)
                raw_llm = raw
                llm_body = validate_body_output(raw)
                if llm_body:
                    llm_ok = True
                    break
            except Exception as e:
                logger.warning("llm_attempt_failed", extra={"id": question.id, "attempt": attempt, "error": str(e)})
        ms_llm = round((time.perf_counter() - t0) * 1000)

        if llm_ok:
            # Override pre_filled vào body LLM (rule-based chắc chắn hơn LLM cho date/org)
            for k, v in pre_filled.items():
                llm_body[k] = v
            body = llm_body
            print(f"[api_v2] id={question.id}  llm={ms_llm}ms  keys={list(body.keys())}")
        else:
            body = _build_fallback_body(top1, pre_filled)
            logger.warning("llm_failed_use_fallback", extra={"id": question.id})
            print(f"[api_v2] id={question.id}  llm=FAILED → fallback body")

    # S4: Coerce + order
    body = _coerce_and_order(body, top1)

    time_response = round(time.perf_counter() - t_start, 3)
    print(f"[api_v2] id={question.id}  TOTAL={time_response:.2f}s")
    print(f"[api_v2] id={question.id}  body={json.dumps(body, ensure_ascii=False)}")

    return {
        "id": question.id,
        "function_code": "call_api",
        "function_result": json.dumps(body, ensure_ascii=False),
        "api_path": top1.path,
        "raw_llm": raw_llm,
        "time_response": time_response,
    }
