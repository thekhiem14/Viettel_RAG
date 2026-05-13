from __future__ import annotations

import json
import re


def validate_body_output(raw: str) -> dict:
    """Parse LLM output thành body dict.

    Tier 1: strict json.loads
    Tier 2: regex extract first {...} block
    Tier 3: fallback body rỗng
    """
    def _try_parse(text: str) -> dict | None:
        try:
            parsed = json.loads(text)
            return parsed if isinstance(parsed, dict) else None
        except (json.JSONDecodeError, TypeError):
            return None

    result = _try_parse(raw)
    if result is not None:
        return result

    match = re.search(r"\{[\s\S]*\}", raw)
    if match:
        result = _try_parse(match.group())
        if result is not None:
            return result

    return {}
