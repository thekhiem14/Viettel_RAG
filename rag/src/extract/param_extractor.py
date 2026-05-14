from __future__ import annotations

import re
import unicodedata

from rag.src.extract.alias_matcher import match_aliases
from rag.src.extract.date_parser import parse_period


def _norm_lower(text: str) -> str:
    return unicodedata.normalize("NFC", text).strip().lower()


def _extract_type(q_lower: str) -> int | None:
    """type: ngày=1, tuần=2, tháng=3, quý=4, năm=5.

    Suy ra từ đơn vị thời gian rõ ràng nhất trong câu hỏi.
    """
    if re.search(r"\bn[ăa]m\s*\d{4}\b", q_lower) and not re.search(r"t\d|qu[ýy]|th[áa]ng", q_lower):
        return 5
    if re.search(r"qu[ýy]\s*\d|\bq\d/", q_lower):
        return 4
    if re.search(r"\bt\d{1,2}/|th[áa]ng\s*\d", q_lower):
        return 3
    if "tuần" in q_lower:
        return 2
    if "ngày" in q_lower and not re.search(r"\bt\d|qu[ýy]|n[ăa]m", q_lower):
        return 1
    return None


def _extract_sort(q_lower: str) -> int | None:
    """sort: tăng dần=1, giảm dần=2. xếp hạng/ranking thường ngụ ý giảm dần."""
    if "tăng dần" in q_lower:
        return 1
    if "giảm dần" in q_lower or "xếp hạng" in q_lower or "ranking" in q_lower:
        return 2
    return None


def _extract_standard_comparison(q_lower: str) -> int | None:
    """standardComparison: trên/vượt ngưỡng=1, dưới ngưỡng=2."""
    if re.search(r"v[ưu][ơo]̣?t|tr[êe]n ng[ưu][ơo]̃?ng|cao h[ơo]n ng[ưu][ơo]̃?ng", q_lower):
        return 1
    if re.search(r"d[ưu][ơo]́?i ng[ưu][ơo]̃?ng|th[âa]́?p h[ơo]n ng[ưu][ơo]̃?ng", q_lower):
        return 2
    return None


def _extract_is_company(q_lower: str) -> bool | None:
    """isCompany=True khi câu hỏi nói 'cả công ty', 'toàn công ty', 'của công ty'."""
    if re.search(r"c[ảa] c[ôo]ng ty|to[àa]n c[ôo]ng ty", q_lower):
        return True
    return None


def extract_all(question: str) -> dict:
    """Trích toàn bộ thông tin có cấu trúc từ câu hỏi.

    Trả về dict có thể chứa các key:
      - fromDate, toDate
      - organization, projectType, projectStatus, level, position, ...
      - projectList (list[int]), customerList (list[str])
      - type, sort, standardComparison (int)
      - isCompany (bool)
    """
    out: dict = {}
    q_lower = _norm_lower(question)

    # 1) Date
    period = parse_period(question)
    if period:
        out.update(period)

    # 2) Aliases (organization + enum params + project_info + customerList)
    out.update(match_aliases(question))

    # 3) Numeric/bool fields
    t = _extract_type(q_lower)
    if t is not None:
        out["type"] = t

    s = _extract_sort(q_lower)
    if s is not None:
        out["sort"] = s

    sc = _extract_standard_comparison(q_lower)
    if sc is not None:
        out["standardComparison"] = sc

    ic = _extract_is_company(q_lower)
    if ic is not None:
        out["isCompany"] = ic

    return out
