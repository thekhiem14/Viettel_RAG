from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
from shared.types import APIEntry


def validate_api_output(
    raw: str,
    candidates: list[APIEntry],
) -> dict:
    """3-tier JSON validation cho call_api output.

    Tier 1: strict json.loads → validate func_code ∈ candidates
    Tier 2: regex extract first {...} block → retry parse
    Tier 3: best-effort → dùng top-1 candidate + body rỗng

    Returns:
        dict với keys: func_code, path, body
    """
    valid_codes = {e.func_code: e for e in candidates}
    top1 = candidates[0]

    def _make_result(func_code: str, path: str, body: dict) -> dict:
        return {"func_code": func_code, "path": path, "body": body}

    def _try_parse(text: str) -> dict | None:
        try:
            parsed = json.loads(text)
            if not isinstance(parsed, dict):
                return None
            fc = parsed.get("func_code", "")
            if fc not in valid_codes:
                return None
            entry = valid_codes[fc]
            body = parsed.get("body", {})
            if not isinstance(body, dict):
                body = {}
            path = parsed.get("path", entry.path)
            return _make_result(fc, path, body)
        except (json.JSONDecodeError, TypeError):
            return None

    # Tier 1: strict parse
    result = _try_parse(raw)
    if result:
        return result

    # Tier 2: regex extract first JSON object
    match = re.search(r"\{[\s\S]*\}", raw)
    if match:
        result = _try_parse(match.group())
        if result:
            return result

    # Tier 3: best-effort — top-1 candidate, body rỗng
    return _make_result(top1.func_code, top1.path, {})
