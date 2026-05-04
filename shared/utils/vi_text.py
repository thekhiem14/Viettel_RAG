from __future__ import annotations

from functools import lru_cache

from pyvi import ViTokenizer


@lru_cache(maxsize=10_000)
def segment(text: str) -> list[str]:
    """Word-segment tiếng Việt, trả về list token lowercase.

    Cache 10k entries — query lặp lại không segment lại.
    Dùng trước khi index BM25 và trước khi search BM25.
    """
    return ViTokenizer.tokenize(text).lower().split()


def segment_text(text: str) -> str:
    """Trả về string đã segment (dùng khi cần string thay vì list)."""
    return " ".join(segment(text))