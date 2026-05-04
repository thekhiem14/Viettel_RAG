from __future__ import annotations

import sys
from pathlib import Path

from rapidfuzz import fuzz, process

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
from shared.types import RetrievalHit
from shared.utils.io import load_json, save_json


class FuzzyStore:
    """RapidFuzz WRatio matching trên name + description (tiếng Việt) của API entries.

    Bắt partial match khi user gõ gần đúng tên API tiếng Việt.
    Ví dụ: "leakage rate theo dự án" → get_leakage_rate_by_project
    """

    def __init__(self) -> None:
        self._targets: list[dict] = []   # [{id, text}]
        self._texts: list[str] = []      # pre-extracted để rapidfuzz không extract lại

    def build(self, targets: list[dict]) -> None:
        """
        Args:
            targets: list of {"id": func_code, "text": "name description"}
        """
        self._targets = targets
        self._texts = [t["text"] for t in targets]

    def save(self, path: Path) -> None:
        save_json(path, self._targets)

    def load(self, path: Path) -> None:
        self._targets = load_json(path)
        self._texts = [t["text"] for t in self._targets]

    def search(self, query: str, top_k: int) -> list[RetrievalHit]:
        """Fuzzy match query với tất cả targets, trả về top_k."""
        results = process.extract(
            query,
            self._texts,
            scorer=fuzz.WRatio,
            limit=top_k,
        )
        hits: list[RetrievalHit] = []
        for rank, (_, score, idx) in enumerate(results):
            hits.append(RetrievalHit(
                id=self._targets[idx]["id"],
                score=score / 100.0,   # normalize về [0, 1]
                source="fuzzy",
                rank=rank,
            ))
        return hits
