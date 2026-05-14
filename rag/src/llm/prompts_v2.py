from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from shared.types import APIEntry


def _format_missing_params(
    candidate: APIEntry, missing_keys: list[str]
) -> str:
    """Liệt kê CHỈ các param còn thiếu, kèm type + description."""
    all_params = {p["name"]: p for p in candidate.required_params + candidate.optional_params if "name" in p}
    lines = []
    for k in missing_keys:
        p = all_params.get(k)
        if not p:
            lines.append(f"  - {k} (unknown type)")
            continue
        desc = p.get("description", "")
        lines.append(f"  - {k} ({p.get('type', '?')}): {desc}")
    return "\n".join(lines) if lines else "  (none)"


def build_api_prompt_v2(
    question: str,
    candidate: APIEntry,
    body_draft: dict,
    missing_keys: list[str],
) -> str:
    """Prompt v2: LLM CHỈ điền các key còn thiếu, không sửa body_draft.

    Args:
        question: câu hỏi gốc tiếng Việt
        candidate: top-1 APIEntry
        body_draft: body đã build bằng rule-based (đa số đã đúng)
        missing_keys: danh sách key cần LLM điền

    Returns:
        Prompt string. Output mong đợi: JSON CHỈ chứa các missing_keys.
    """
    missing_text = _format_missing_params(candidate, missing_keys)
    draft_json = json.dumps(body_draft, ensure_ascii=False, indent=2)

    return f"""Bạn là API body completer. Body JSON đã được build sẵn từ rule-based extraction.
Nhiệm vụ: CHỈ điền giá trị cho các key còn thiếu, KHÔNG sửa các key đã có.

Câu hỏi: {question}

API: {candidate.name}
Description: {candidate.description}

Body đã có sẵn (KHÔNG sửa):
{draft_json}

Các key CẦN ĐIỀN (chỉ trả về JSON chứa đúng các key này):
{missing_text}

Quy tắc:
- Ngày tháng dạng yyyy-mm-dd.
- Param `type`: ngày=1, tuần=2, tháng=3, quý=4, năm=5.
- Param `sort`: tăng dần=1, giảm dần=2.
- Param `standardComparison`: trên/vượt ngưỡng=1, dưới ngưỡng=2.
- List rỗng = [], string rỗng = "", không biết = null.
- KHÔNG thêm key ngoài danh sách trên.
- KHÔNG giải thích, CHỈ trả về 1 JSON hợp lệ chứa các key cần điền.

JSON:"""
