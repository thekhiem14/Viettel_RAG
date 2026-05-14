from __future__ import annotations

from rag.src.extract.alias_matcher import match_aliases
from rag.src.extract.date_parser import parse_period


def extract_all(question: str) -> dict:
    """Trích thông tin có cấu trúc deterministic từ câu hỏi.

    Chỉ extract những gì rule-based làm được chắc chắn:
      - fromDate, toDate  (regex)
      - organization      (exact match viết tắt)
      - projectList       (tra bảng tên → id)
      - customerList      (match tên công ty dài)

    Tất cả params còn lại (type, sort, projectType, lcntType, ...) để LLM
    đọc description trong schema và tự điền.
    """
    out: dict = {}

    period = parse_period(question)
    if period:
        out.update(period)

    out.update(match_aliases(question))

    return out
