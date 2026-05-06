from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
from shared.types import APIEntry, Chunk


def _format_params(params: list[dict]) -> str:
    if not params:
        return "  (none)"
    lines = []
    for p in params:
        lines.append(f"  - {p['name']} ({p['type']}): {p.get('description', '')}")
    return "\n".join(lines)


def _format_api_entry(idx: int, entry: APIEntry) -> str:
    required = _format_params(entry.required_params)
    optional = _format_params(entry.optional_params)
    return (
        f"[{idx}] func_code: {entry.func_code}\n"
        f"    Tên: {entry.name}\n"
        f"    Mô tả: {entry.description}\n"
        f"    Path: {entry.path}\n"
        f"    Required params:\n{required}\n"
        f"    Optional params:\n{optional}"
    )


def build_api_prompt(question: str, candidates: list[APIEntry]) -> str:
    """Tạo prompt cho call_api: LLM chọn 1 trong top-5 candidates và điền params.

    Args:
        question: câu hỏi tiếng Việt của user
        candidates: danh sách APIEntry (thường top-5 từ retriever)

    Returns:
        Prompt string để pass vào qwen.generate()
    """
    api_blocks = "\n\n".join(
        _format_api_entry(i + 1, entry) for i, entry in enumerate(candidates)
    )

    func_codes = ", ".join(e.func_code for e in candidates)

    return f"""Bạn là trợ lý AI chuyên về hệ thống quản lý dự án Viettel. Câu hỏi: {question}

Dưới đây là {len(candidates)} API có thể phù hợp. Hãy chọn API đúng nhất và điền params từ câu hỏi:

{api_blocks}

Hướng dẫn:
- Chọn đúng 1 func_code trong danh sách: {func_codes}
- Điền body từ thông tin trong câu hỏi (ngày tháng dùng format yyyy-mm-dd)
- Nếu câu hỏi không đề cập đến một param nào đó, dùng [] cho List, null cho các kiểu khác
- Chỉ trả về JSON, không giải thích thêm

Trả về JSON theo format sau:
{{
  "func_code": "<chọn 1 trong {len(candidates)} func_code ở trên>",
  "path": "<path tương ứng với func_code đã chọn>",
  "body": {{}}
}}"""


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

Hãy lập luận ngắn gọn dựa vào tài liệu, rồi trả lời bằng chữ cái đáp án (có thể nhiều chữ cái nếu câu hỏi cho phép nhiều đáp án, ví dụ: AB).
Đáp án:"""
