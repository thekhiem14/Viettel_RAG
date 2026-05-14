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
    """Default value cho param khi chưa có giá trị nào."""
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


def _assemble_body(candidate: APIEntry, extracted: dict) -> tuple[dict, list[str]]:
    """Build body từ example_body + extracted, trả về (body, missing_required_keys).

    - Bắt đầu từ candidate.example_body (đã đúng schema)
    - Ghi đè bằng giá trị trong extracted nếu khớp key
    - Required nào sau bước trên vẫn rỗng → đưa vào missing_keys cho LLM
    """
    # Schema definitions
    required = candidate.required_params or []
    optional = candidate.optional_params or []
    schema_params = {p["name"]: p for p in required + optional if "name" in p}
    valid_keys = set(schema_params.keys())

    # Start from example_body (chỉ giữ key thuộc schema)
    body: dict = {}
    if candidate.example_body and isinstance(candidate.example_body, dict):
        for k, v in candidate.example_body.items():
            if k in valid_keys:
                body[k] = v

    # Đảm bảo mọi key trong schema đều có mặt (với default phù hợp)
    for k, p in schema_params.items():
        if k not in body:
            body[k] = _default_for_type(p.get("type", ""))

    # Override bằng extracted
    for k, v in extracted.items():
        if k in valid_keys:
            body[k] = v

    # Tìm required còn thiếu giá trị thực
    missing: list[str] = []
    for p in required:
        name = p.get("name")
        if not name:
            continue
        val = body.get(name)
        is_empty = (
            val is None
            or (isinstance(val, str) and val == "")
            or (isinstance(val, list) and len(val) == 0 and "date" in (p.get("type", "") or "").lower())
        )
        # Đặc biệt: List<...> rỗng được CHẤP NHẬN nếu câu hỏi không đề cập (theo schema desc)
        # Chỉ coi là missing nếu Date hoặc Int/Bool/String required mà rỗng
        ptype = (p.get("type") or "").lower()
        if "list" in ptype:
            continue  # list rỗng là hợp lệ
        if is_empty:
            missing.append(name)

    return body, missing


def _coerce_types(body: dict, candidate: APIEntry) -> dict:
    """Ép kiểu cuối cùng theo schema, lọc key lạ, giữ thứ tự example_body."""
    schema_params = {
        p["name"]: p
        for p in (candidate.required_params or []) + (candidate.optional_params or [])
        if "name" in p
    }
    valid_keys = set(schema_params.keys())

    coerced: dict = {}
    for k, v in body.items():
        if k not in valid_keys:
            continue
        ptype = (schema_params[k].get("type") or "").lower()
        if "list" in ptype:
            if v is None:
                v = []
            elif not isinstance(v, list):
                v = [v]
        elif "bool" in ptype:
            if isinstance(v, str):
                v = {"true": True, "false": False}.get(v.lower(), None)
        elif "int" in ptype or "long" in ptype:
            if isinstance(v, str) and v.isdigit():
                v = int(v)
        elif "date" in ptype:
            if not isinstance(v, str):
                v = ""
        coerced[k] = v

    # Order: theo example_body trước, sau đó required, sau đó optional
    order: list[str] = []
    seen: set[str] = set()
    if candidate.example_body and isinstance(candidate.example_body, dict):
        for k in candidate.example_body.keys():
            if k in coerced and k not in seen:
                order.append(k)
                seen.add(k)
    for p in (candidate.required_params or []) + (candidate.optional_params or []):
        k = p.get("name")
        if k and k in coerced and k not in seen:
            order.append(k)
            seen.add(k)
    return {k: coerced[k] for k in order}


def run(question: Question) -> dict:
    """Chạy call_api pipeline v2 cho 1 câu hỏi.

    Returns:
        dict: {id, function_code, function_result, time_response}
        function_result là JSON pretty-print: {"path": ..., "body": {...}}
    """
    t_start = time.perf_counter()
    retriever = _get_retriever()
    schemas = _get_schemas()

    # S1+S2: Retrieval
    t0 = time.perf_counter()
    hits = retriever.search(question.question)
    candidates: list[APIEntry] = [schemas[h.id] for h in hits if h.id in schemas]
    if not candidates:
        candidates = list(schemas.values())[: config.API_RETRIEVE_TOP_K]
    ms_ret = round((time.perf_counter() - t0) * 1000)
    top1 = candidates[0]
    logger.info(
        "stage_retrieval",
        extra={"id": question.id, "n_candidates": len(candidates), "top1": top1.func_code, "ms": ms_ret},
    )
    print(f"[api_v2] id={question.id}  retrieval={ms_ret}ms  top1={top1.func_code}")

    # S3: Structured extraction (rule-based)
    t0 = time.perf_counter()
    extracted = extract_all(question.question)
    ms_ext = round((time.perf_counter() - t0) * 1000)
    logger.info("stage_extract", extra={"id": question.id, "keys": list(extracted.keys()), "ms": ms_ext})
    print(f"[api_v2] id={question.id}  extract={ms_ext}ms  keys={list(extracted.keys())}")

    # S4: Schema-driven assembly
    body, missing = _assemble_body(top1, extracted)
    print(f"[api_v2] id={question.id}  draft_keys={list(body.keys())}  missing_required={missing}")

    # S5: LLM refine (chỉ khi còn missing required HOẶC SKIP_LLM=False và missing)
    if missing and not config.SKIP_LLM:
        t0 = time.perf_counter()
        prompt = build_api_prompt_v2(question.question, top1, body, missing)
        try:
            raw_output = generate(prompt)
            patch = validate_body_output(raw_output)
            # Chỉ merge key thuộc missing
            for k in missing:
                if k in patch:
                    body[k] = patch[k]
            ms_llm = round((time.perf_counter() - t0) * 1000)
            logger.info("stage_llm", extra={"id": question.id, "filled": list(patch.keys()), "ms": ms_llm})
            print(f"[api_v2] id={question.id}  llm={ms_llm}ms  filled={list(patch.keys())}")
        except Exception as e:
            logger.warning("llm_failed", extra={"id": question.id, "error": str(e)})
            print(f"[api_v2] id={question.id}  llm=FAILED keep_draft  err={e}")
    else:
        logger.info("stage_llm_skipped", extra={"id": question.id, "reason": "no_missing" if not missing else "SKIP_LLM"})
        print(f"[api_v2] id={question.id}  llm=SKIPPED  ({'no missing' if not missing else 'SKIP_LLM'})")

    # S6: Validate + coerce + order
    body = _coerce_types(body, top1)

    result = {"path": top1.path, "body": body}
    time_response = round(time.perf_counter() - t_start, 3)
    print(f"[api_v2] id={question.id}  TOTAL={time_response:.2f}s")

    return {
        "id": question.id,
        "function_code": "call_api",
        "function_result": json.dumps(result, ensure_ascii=False, indent=2),
        "time_response": time_response,
    }
