"""call_api pipeline v2.

Flow tổng quan:
  S1. Retrieval         → top-1 APIEntry phù hợp câu hỏi
  S2. Rule-based extract → pre_filled (date, organization, projectList, ...)
  S3. LLM fill body      → đọc description, sinh JSON body đầy đủ key
  S4. Coerce + order     → ép kiểu, giữ null/[], sort key theo schema

Pre_filled luôn override LLM body (rule-based chắc chắn hơn cho date/org).
Fallback: nếu LLM fail 2 lần → dùng example_body + default theo type.
"""
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

# Số lần retry LLM khi parse body fail
_LLM_MAX_ATTEMPTS = 2

# ──────────────────────────────────────────────────────────────────────────────
# Lazy singletons
# ──────────────────────────────────────────────────────────────────────────────

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


# ──────────────────────────────────────────────────────────────────────────────
# Helpers — schema introspection
# ──────────────────────────────────────────────────────────────────────────────

def _schema_params(candidate: APIEntry) -> dict[str, dict]:
    """Map {param_name: param_dict} gộp required + optional theo thứ tự schema."""
    all_params = (candidate.required_params or []) + (candidate.optional_params or [])
    return {p["name"]: p for p in all_params if "name" in p}


def _default_for_type(type_str: str):
    """Default value cho 1 param dựa trên kiểu khai báo trong schema."""
    t = (type_str or "").lower()
    if "list" in t:
        return []
    if "date" in t or "string" in t:
        return ""
    # bool, int, long → None
    return None


# ──────────────────────────────────────────────────────────────────────────────
# Body builders
# ──────────────────────────────────────────────────────────────────────────────

def _build_fallback_body(candidate: APIEntry, pre_filled: dict) -> dict:
    """Body cho trường hợp LLM fail: example_body → default → pre_filled override."""
    params = _schema_params(candidate)
    valid_keys = set(params.keys())
    body: dict = {}

    # 1) Seed từ example_body (chỉ key hợp lệ)
    if isinstance(candidate.example_body, dict):
        for k, v in candidate.example_body.items():
            if k in valid_keys:
                body[k] = v

    # 2) Fill key còn thiếu bằng default theo type
    for k, p in params.items():
        if k not in body:
            body[k] = _default_for_type(p.get("type", ""))

    # 3) Override bằng pre_filled (rule-based luôn thắng)
    for k, v in pre_filled.items():
        if k in valid_keys:
            body[k] = v
    return body


def _coerce_value(value, ptype: str):
    """Ép value về đúng kiểu schema. Giữ null/[] thay vì drop."""
    t = ptype.lower()

    if "list" in t:
        if value is None:
            return []
        if isinstance(value, str):
            return [value] if value else []
        if not isinstance(value, list):
            return [value]
        return value

    if "bool" in t and isinstance(value, str):
        return {"true": True, "false": False}.get(value.lower())

    if ("int" in t or "long" in t) and isinstance(value, str):
        return int(value) if value.lstrip("-").isdigit() else None

    if "date" in t and not isinstance(value, str):
        return ""

    return value


def _coerce_and_order(body: dict, candidate: APIEntry) -> dict:
    """Ép kiểu mọi key + giữ thứ tự required-before-optional theo schema."""
    params = _schema_params(candidate)
    ordered: dict = {}
    for name, p in params.items():
        ordered[name] = _coerce_value(body.get(name), p.get("type", ""))
    return ordered


# ──────────────────────────────────────────────────────────────────────────────
# Stages
# ──────────────────────────────────────────────────────────────────────────────

def _stage_retrieval(question: Question) -> tuple[APIEntry, int]:
    """S1: search top-1 APIEntry. Fallback: first N schema entries."""
    t0 = time.perf_counter()
    schemas = _get_schemas()
    hits = _get_retriever().search(question.question)
    candidates = [schemas[h.id] for h in hits if h.id in schemas]
    if not candidates:
        candidates = list(schemas.values())[:config.API_RETRIEVE_TOP_K]
    ms = round((time.perf_counter() - t0) * 1000)
    return candidates[0], ms


def _stage_extract(question: Question) -> tuple[dict, int]:
    """S2: rule-based extract date/organization/projectList từ câu hỏi."""
    t0 = time.perf_counter()
    pre_filled = extract_all(question.question)
    ms = round((time.perf_counter() - t0) * 1000)
    return pre_filled, ms


def _stage_llm_body(
    question: Question,
    top1: APIEntry,
    pre_filled: dict,
) -> tuple[dict, str, int, bool]:
    """S3: LLM sinh body, retry tối đa _LLM_MAX_ATTEMPTS.

    Returns (body, raw_llm_last, ms, llm_ok).
    Nếu LLM ok → override pre_filled vào body trước khi trả về.
    Nếu fail → build fallback body từ example + default + pre_filled.
    """
    t0 = time.perf_counter()
    prompt = build_api_prompt_v2(question.question, top1, pre_filled)

    raw_llm = ""
    llm_body: dict | None = None
    for attempt in range(_LLM_MAX_ATTEMPTS):
        try:
            raw_llm = generate(prompt)
            parsed = validate_body_output(raw_llm)
            if parsed:
                llm_body = parsed
                break
        except Exception as e:
            logger.warning(
                "llm_attempt_failed",
                extra={"id": question.id, "attempt": attempt, "error": str(e)},
            )

    ms = round((time.perf_counter() - t0) * 1000)

    if llm_body is not None:
        # Rule-based pre_filled luôn thắng LLM (date/org chắc chắn hơn)
        for k, v in pre_filled.items():
            llm_body[k] = v
        return llm_body, raw_llm, ms, True

    # LLM fail → fallback
    #logger.warning("llm_failed_use_fallback", extra={"id": question.id})
    return _build_fallback_body(top1, pre_filled), raw_llm, ms, False


# ──────────────────────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────────────────────

def run(question: Question) -> dict:
    """Chạy full pipeline cho 1 câu hỏi → dict kết quả chuẩn cho orchestrator."""
    t_start = time.perf_counter()

    # S1: Retrieval
    top1, ms_ret = _stage_retrieval(question)
    # #logger.info("stage_retrieval", extra={"id": question.id, "top1": top1.func_code, "ms": ms_ret})
    #print(f"[api_v2] id={question.id}  retrieval={ms_ret}ms  top1={top1.func_code}")

    # S2: Rule-based extract
    pre_filled, ms_ext = _stage_extract(question)
    #print(f"[api_v2] id={question.id}  extract={ms_ext}ms  pre_filled={list(pre_filled.keys())}")

    # S3: LLM fill body (+ override pre_filled, hoặc fallback)
    body, raw_llm, ms_llm, llm_ok = _stage_llm_body(question, top1, pre_filled)
    #print(f"[api_v2] id={question.id}  raw_llm={raw_llm!r}")
    # if llm_ok:
        #print(f"[api_v2] id={question.id}  llm={ms_llm}ms  keys={list(body.keys())}")
    # else:
        #print(f"[api_v2] id={question.id}  llm=FAILED → fallback body")

    # S4: Coerce + order theo schema
    body = _coerce_and_order(body, top1)

    # Build func_param chuẩn submission format (không gồm func_code — đã có ở cột func_code riêng)
    func_param = {"path": top1.path, "body": body}
    time_response = round(time.perf_counter() - t_start, 3)
    #print(f"[api_v2] id={question.id}  TOTAL={time_response:.2f}s")
    #print(f"[api_v2] id={question.id}  body={json.dumps(body, ensure_ascii=False)}")

    return {
        "id": question.id,
        "function_code": "call_api",
        "function_result": json.dumps(func_param, ensure_ascii=False),
        "raw_llm": raw_llm,
        "time_response": time_response,
    }
