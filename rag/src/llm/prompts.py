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


_LOOKUP_PARAMS = {"projectId", "projectList", "customerList"}


def _format_params(params: list[dict], aliases: dict[str, list[dict]], question: str = "") -> str:
    if not params:
        return "  (none)"
    lines = []
    for p in params:
        name = p["name"]
        desc = p.get("description", "")
        entries = aliases.get(name, [])
        if entries:
            # Lookup params: chỉ inject entries khớp câu hỏi thay vì toàn bộ
            if name in _LOOKUP_PARAMS and question:
                entries = [e for e in entries if str(e.get("key", "")) in question]
            seen: list[str] = []
            for v in entries:
                val = str(v.get("value", v.get("key", "")))
                if val and val not in seen:
                    seen.append(val)
            if seen:
                valid = ", ".join(seen)
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
    required_text = _format_params(candidate.required_params, aliases, question)
    optional_text = _format_params(candidate.optional_params, aliases, question)

    return f"""Bạn là API body generator. Sinh body JSON cho API dưới đây dựa vào câu hỏi tiếng Việt.

Câu hỏi: {question}

API: {candidate.name}
Description: {candidate.description}

Required params (BẮT BUỘC phải có trong body):
{required_text}

Optional params (chỉ thêm vào body nếu câu hỏi đề cập; default [] cho List, null cho kiểu khác):
{optional_text}

Ghi chú quan trọng:
- Ngày tháng dạng yyyy-mm-dd. Quy ước:
  * "năm YYYY" → fromDate=YYYY-01-01, toDate=YYYY-12-31
  * "Quý N/YYYY" hoặc "QN/YYYY" → quý N (Q1=01-01..03-31, Q2=04-01..06-30, Q3=07-01..09-30, Q4=10-01..12-31)
  * "Tháng N/YYYY" hoặc "TN/YYYY" → ngày 1 đến ngày cuối của tháng N
  * "TM/YYYY - TN/YYYY" hoặc "TM/YYYY -> TN/YYYY" → từ đầu tháng M đến cuối tháng N
- Param `type`: ngày=1, tuần=2, tháng=3, quý=4, năm=5. Khi câu hỏi đề cập khoảng nhiều tháng/không rõ → 3.
- Param `standardComparison`: trên/vượt ngưỡng=1, dưới ngưỡng=2.
- Param `sort`: tăng dần=1, giảm dần=2.
- KHÔNG thêm key nào ngoài danh sách required + optional ở trên.
- KHÔNG giải thích, chỉ trả về 1 JSON body hợp lệ.

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
