from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from shared.types import APIEntry


def _format_params(params: list[dict]) -> str:
    if not params:
        return "  (none)"
    lines = []
    for p in params:
        name = p.get("name", "")
        ptype = p.get("type", "?")
        desc = p.get("description", "")
        lines.append(f"  - {name} ({ptype}): {desc}")
    return "\n".join(lines)


def build_api_prompt_v2(
    question: str,
    candidate: APIEntry,
    pre_filled: dict,
) -> str:
    """Prompt v2: LLM fill toàn bộ body dựa vào schema description.

    Args:
        question:    câu hỏi gốc tiếng Việt
        candidate:   top-1 APIEntry (có đầy đủ required/optional params + description)
        pre_filled:  dict các giá trị đã extract bằng rule-based
                     (fromDate, toDate, organization, projectList, ...)
                     LLM KHÔNG được sửa các key này.

    Returns:
        Prompt string. Output mong đợi: JSON body hoàn chỉnh đúng schema.
    """
    required_text = _format_params(candidate.required_params)
    optional_text = _format_params(candidate.optional_params)
    pre_filled_json = json.dumps(pre_filled, ensure_ascii=False, indent=2)

    # Liệt kê tên tất cả key để LLM biết phải có đủ
    all_keys = [p["name"] for p in (candidate.required_params or []) + (candidate.optional_params or []) if "name" in p]
    keys_list = ", ".join(all_keys)

    return f"""Bạn là API body generator. Hãy sinh JSON body cho API dưới đây dựa vào câu hỏi tiếng Việt.

Câu hỏi: {question}

API: {candidate.name}
Mô tả: {candidate.description}

REQUIRED params (bắt buộc phải có):
{required_text}

OPTIONAL params (phải có trong body, dùng giá trị mặc định nếu câu hỏi không đề cập):
{optional_text}

Các giá trị đã được extract sẵn (KHÔNG thay đổi):
{pre_filled_json}

Yêu cầu:
1. Chỉ trả về nội dung bên trong body — tức là object JSON với các key: {keys_list}
2. KHÔNG wrap thêm {{"path": ..., "body": ...}} bên ngoài.
3. Với mỗi param, đọc kỹ description để chọn giá trị đúng.
4. Nếu câu hỏi KHÔNG đề cập đến một optional param → dùng giá trị mặc định theo description (thường là [] cho List, null cho Integer/Boolean).
5. Không thêm key ngoài danh sách trên.
6. Không giải thích, chỉ trả về 1 JSON object hợp lệ.

Ví dụ output đúng: {{"key1": "value1", "key2": []}}

Body:"""
