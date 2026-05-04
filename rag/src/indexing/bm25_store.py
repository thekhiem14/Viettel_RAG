from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from rank_bm25 import BM25Okapi

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
import config
from shared.types import RetrievalHit
from shared.utils.io import load_pickle, save_pickle
from shared.utils.vi_text import segment


class BM25Store:
    """BM25Okapi với pyvi word-segmentation cho tiếng Việt.

    Persist cả segmented corpus để không segment lại khi load.
    """

    def __init__(self) -> None:
        self._bm25: BM25Okapi | None = None
        self._ids: list[str] = []
        self._corpus: list[list[str]] = []  # segmented tokens

    def build(self, texts: list[str], ids: list[str]) -> None:
        """Build BM25 từ raw texts (sẽ tự segment bằng pyvi)."""
        self._ids = list(ids)
        self._corpus = [segment(t) for t in texts]
        self._bm25 = BM25Okapi(self._corpus)

    def save(self, path: Path) -> None:
        save_pickle(path, {"bm25": self._bm25, "ids": self._ids, "corpus": self._corpus})

    def load(self, path: Path) -> None:
        data = load_pickle(path)
        self._bm25 = data["bm25"]
        self._ids = data["ids"]
        self._corpus = data["corpus"]

    def search(self, query: str, top_k: int) -> list[RetrievalHit]:
        """Search BM25 — query cũng được segment trước khi match."""
        tokenized_query = segment(query)
        scores: np.ndarray = self._bm25.get_scores(tokenized_query)

        top_indices = np.argsort(scores)[::-1][:top_k]
        hits: list[RetrievalHit] = []
        for rank, idx in enumerate(top_indices):
            if scores[idx] <= 0:
                break
            hits.append(RetrievalHit(
                id=self._ids[idx],
                score=float(scores[idx]),
                source="bm25",
                rank=rank,
            ))
        return hits
