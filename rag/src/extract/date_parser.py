from __future__ import annotations

import calendar
import re
import unicodedata


_QUARTER_RANGES = {
    1: ("01-01", "03-31"),
    2: ("04-01", "06-30"),
    3: ("07-01", "09-30"),
    4: ("10-01", "12-31"),
}


def _norm(text: str) -> str:
    return unicodedata.normalize("NFC", text).strip()


def _month_range(year: int, month: int) -> tuple[str, str]:
    last_day = calendar.monthrange(year, month)[1]
    return f"{year:04d}-{month:02d}-01", f"{year:04d}-{month:02d}-{last_day:02d}"


def _range_months(year_from: int, month_from: int, year_to: int, month_to: int) -> tuple[str, str]:
    from_date = f"{year_from:04d}-{month_from:02d}-01"
    last_day = calendar.monthrange(year_to, month_to)[1]
    to_date = f"{year_to:04d}-{month_to:02d}-{last_day:02d}"
    return from_date, to_date


def parse_period(question: str) -> dict | None:
    """Parse khoảng thời gian từ câu hỏi tiếng Việt.

    Trả về {"fromDate": "yyyy-mm-dd", "toDate": "yyyy-mm-dd"} hoặc None.

    Hỗ trợ các mẫu (theo example_data thực tế):
      - "năm YYYY"
      - "Quý N/YYYY" | "QN/YYYY" | "quý N/YYYY"
      - "Tháng N/YYYY" | "TN/YYYY" | "T0N/YYYY" | "tháng N năm YYYY"
      - "TM/YYYY -> TN/YYYY" | "TM/YYYY - TN/YYYY"
      - "khoảng từ TM/YYYY - TN/YYYY"
    """
    q = _norm(question)
    q_lower = q.lower()

    # 1) Range tháng: "T1/2025 - T7/2025", "T6/2025 -> T12/2025", "T01/2025 -> T12/2025"
    m = re.search(
        r"t(?:h[áa]ng)?\s*0?(\d{1,2})\s*/\s*(\d{4})\s*(?:->|-|—|đến|toi|tới)\s*t(?:h[áa]ng)?\s*0?(\d{1,2})\s*/\s*(\d{4})",
        q_lower,
    )
    if m:
        mf, yf, mt, yt = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
        if 1 <= mf <= 12 and 1 <= mt <= 12:
            f, t = _range_months(yf, mf, yt, mt)
            return {"fromDate": f, "toDate": t}

    # 2) Quý: "Q3/2025", "Quý 4/2025", "quý 1 năm 2025"
    m = re.search(r"qu[ýy]\s*0?(\d)\s*/\s*(\d{4})", q_lower)
    if not m:
        m = re.search(r"\bq\s*0?(\d)\s*/\s*(\d{4})", q_lower)
    if not m:
        m = re.search(r"qu[ýy]\s*0?(\d)\s*n[ăa]m\s*(\d{4})", q_lower)
    if m:
        qn, year = int(m.group(1)), int(m.group(2))
        if 1 <= qn <= 4:
            frm, to = _QUARTER_RANGES[qn]
            return {"fromDate": f"{year:04d}-{frm}", "toDate": f"{year:04d}-{to}"}

    # 3) Tháng đơn: "T11/2025", "Tháng 12/2025", "tháng 5 năm 2025"
    m = re.search(r"t(?:h[áa]ng)?\s*0?(\d{1,2})\s*/\s*(\d{4})", q_lower)
    if not m:
        m = re.search(r"th[áa]ng\s*0?(\d{1,2})\s*n[ăa]m\s*(\d{4})", q_lower)
    if m:
        month, year = int(m.group(1)), int(m.group(2))
        if 1 <= month <= 12:
            f, t = _month_range(year, month)
            return {"fromDate": f, "toDate": t}

    # 4) Năm đơn: "năm 2025"
    m = re.search(r"n[ăa]m\s*(\d{4})", q_lower)
    if m:
        year = int(m.group(1))
        return {"fromDate": f"{year:04d}-01-01", "toDate": f"{year:04d}-12-31"}

    return None
