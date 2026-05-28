from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from shared.types import Chunk


def build_doc_prompt(chunks: list[Chunk], question: str, options: dict[str, str]) -> str:
    """Tạo prompt CoT cho call_document: LLM chọn đáp án MCQ từ top chunks.

    Args:
        chunks: top chunks sau rerank + section expansion
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

Chỉ trả lời bằng chữ cái đáp án, không giải thích, không suy nghĩ thêm. Chỉ chọn duy nhất 1 đáp án.
Đáp án:"""
