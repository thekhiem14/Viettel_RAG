from __future__ import annotations

import sys
from pathlib import Path

from rapidfuzz import fuzz

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
from shared.types import RetrievalHit
from shared.utils.io import load_json, save_json


class FuzzyStore:
    """RapidFuzz WRatio matching trên name + description (tiếng Việt) của API entries.

    Bắt partial match khi user gõ gần đúng tên API tiếng Việt.
    Ví dụ: "leakage rate theo dự án" → get_leakage_rate_by_project
    """

    def __init__(self) -> None:
        self._targets: list[dict] = []   # [{id, func_code, name, text}]

    def build(self, targets: list[dict]) -> None:
        """
        Args:
            targets: list of {"id": func_code, "text": "name description"}
        """
        self._targets = targets

    def save(self, path: Path) -> None:
        save_json(path, self._targets)

    def load(self, path: Path) -> None:
        self._targets = load_json(path)

    def search(self, query: str, top_k: int) -> list[RetrievalHit]:
        """Fuzzy match query với tất cả targets bằng weighted sum.

        score = 0.5*WRatio(name) + 0.3*WRatio(func_code) + 0.2*WRatio(text)
        """
        scored: list[tuple[str, float]] = []
        for t in self._targets:
            s_name = fuzz.WRatio(query, t["name"]) if "name" in t else 0.0
            s_text = fuzz.WRatio(query, t["text"])
            score = 0.6 * s_name + 0.4 * s_text
            scored.append((t["id"], score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return [
            RetrievalHit(id=hit_id, score=score / 100.0, source="fuzzy", rank=rank)
            for rank, (hit_id, score) in enumerate(scored[:top_k])
        ]
