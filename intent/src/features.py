from __future__ import annotations

import re

_ABCD_RE = re.compile(r"\b[A-D][,.]")
_PUBLIC_RE = re.compile(r"Public_\d+")
_DATE_RANGE_RE = re.compile(r"T\d{1,2}/\d{4}|Q[1-4]/\d{4}|năm\s+\d{4}", re.IGNORECASE)


def has_abcd_pattern(text: str) -> bool:
    """True nếu text chứa A, B, C, D options (dấu hiệu call_document)."""
    return bool(_ABCD_RE.search(text))


def has_public_ref(text: str) -> bool:
    """True nếu text đề cập Public_XXX (dấu hiệu call_document)."""
    return bool(_PUBLIC_RE.search(text))


def has_date_range(text: str) -> bool:
    """True nếu text có khoảng thời gian (T1/2025, Q3/2025, năm 2025) — thường call_api."""
    return bool(_DATE_RANGE_RE.search(text))


def extract_features(question: str, note: str | None = None) -> list[float]:
    """Trả về feature vector số từ question + note.

    Features:
        0: has_abcd_pattern (note)
        1: has_public_ref (question)
        2: has_date_range (question)
        3: note is not None (1.0 = call_document signal)
    """
    combined = f"{question} {note or ''}"
    return [
        float(has_abcd_pattern(note or "")),
        float(has_public_ref(question)),
        float(has_date_range(question)),
        float(note is not None and note.strip().lower() not in {"nan", "none", ""}),
    ]
