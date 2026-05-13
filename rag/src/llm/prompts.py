from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

import config
from shared.types import APIEntry, Chunk

_aliases: dict[str, list[dict]] | None = None


def _load_aliases() -> dict[str, list[dict]]:
    global _aliases
    if _aliases is None:
        try:
            with open(config.API_ALIASES, encoding="utf-8") as f:
                _aliases = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            _aliases = {}
    return _aliases


def _format_params(params: list[dict], aliases: dict[str, list[dict]]) -> str:
    if not params:
        return "  (none)"
    lines = []
    for p in params:
        name = p["name"]
        desc = p.get("description", "")
        enum_values = aliases.get(name)
        if enum_values:
            valid = ", ".join(str(v.get("value", v.get("key", ""))) for v in enum_values)
            desc = f"{desc} [valid values: {valid}]" if desc else f"[valid values: {valid}]"
        lines.append(f"  - {name} ({p['type']}): {desc}")
    return "\n".join(lines)



def build_api_prompt(question: str, candidate: APIEntry) -> str:
    """Tạo prompt cho call_api: LLM điền body cho top-1 candidate.

    Args:
        question: câu hỏi tiếng Việt của user
        candidate: top-1 APIEntry từ retriever

    Returns:
        Prompt string để pass vào qwen.generate()
    """
    aliases = _load_aliases()
    params_text = _format_params(candidate.required_params + candidate.optional_params, aliases)
    example = json.dumps(candidate.example_body, ensure_ascii=False) if candidate.example_body else "{}"

    return f"""Câu hỏi: {question}

API: {candidate.name}
Params:
{params_text}
Example body: {example}

Hướng dẫn:
- Điền body từ thông tin trong câu hỏi theo đúng format example body
- Ngày tháng dùng format yyyy-mm-dd
- Nếu không đề cập, dùng [] cho List, null cho các kiểu khác
- Chỉ trả về JSON body, không giải thích

Body:"""


def build_doc_prompt(chunks: list[Chunk], question: str, options: dict[str, str]) -> str:
    """Tạo prompt CoT cho call_document: LLM chọn đáp án MCQ từ top-5 chunks.

    Args:
        chunks: top-5 chunks sau rerank
        question: câu hỏi MCQ
        options: {"A": "...", "B": "...", "C": "...", "D": "..."}

    Returns:
        Prompt string để pass vào qwen.generate()
    """
    context_blocks = "\n\n".join(
        f"[{i + 1}] {c.text}" for i, c in enumerate(chunks)
    )

    options_text = "   ".join(f"{k}. {v}" for k, v in options.items())

    return f"""Dựa vào các đoạn tài liệu dưới đây, hãy lập luận từng bước rồi chọn đáp án đúng.

{context_blocks}

Câu hỏi: {question}
{options_text}

Chỉ trả lời bằng chữ cái đáp án, không giải thích, không suy nghĩ thêm. Có thể nhiều đáp án, mỗi đáp án cách nhau bằng dấu phẩy (ví dụ: A,B,C,D).
Đáp án:"""
