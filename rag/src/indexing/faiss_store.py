from __future__ import annotations

import sys
from pathlib import Path
from typing import Callable

import faiss
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
from shared.types import RetrievalHit
from shared.utils.io import load_pickle, save_pickle


class FaissStore:
    """FAISS IndexFlatIP — dot product trên L2-normalized vectors = cosine similarity."""

    def __init__(self) -> None:
        self._index: faiss.IndexFlatIP | None = None
        self._ids: list[str] = []

    def build(self, embeddings: np.ndarray, ids: list[str]) -> None:
        """Tạo index từ embeddings (N, D) và danh sách id tương ứng."""
        dim = embeddings.shape[1]
        self._index = faiss.IndexFlatIP(dim)
        self._index.add(embeddings.astype(np.float32))
        self._ids = list(ids)

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        faiss.write_index(self._index, str(path))
        save_pickle(path.with_suffix(".ids.pkl"), self._ids)

    def load(self, path: Path) -> None:
        self._index = faiss.read_index(str(path))
        self._ids = load_pickle(path.with_suffix(".ids.pkl"))

    def search(
        self,
        query_vec: np.ndarray,
        top_k: int,
        filter_fn: Callable[[str], bool] | None = None,
    ) -> list[RetrievalHit]:
        """Tìm top_k kết quả gần nhất.

        Args:
            query_vec: shape (D,) hoặc (1, D), L2-normalized
            top_k: số kết quả trả về
            filter_fn: nếu có, chỉ giữ các id mà filter_fn(id) == True
        """
        q = query_vec.reshape(1, -1).astype(np.float32)

        # Lấy nhiều hơn nếu cần filter
        k = top_k * 10 if filter_fn else top_k
        k = min(k, len(self._ids))

        scores, indices = self._index.search(q, k)
        scores, indices = scores[0], indices[0]

        hits: list[RetrievalHit] = []
        rank = 0
        for score, idx in zip(scores, indices):
            if idx < 0:
                continue
            hit_id = self._ids[idx]
            if filter_fn and not filter_fn(hit_id):
                continue
            hits.append(RetrievalHit(id=hit_id, score=float(score), source="faiss", rank=rank))
            rank += 1
            if rank >= top_k:
                break

        return hits
