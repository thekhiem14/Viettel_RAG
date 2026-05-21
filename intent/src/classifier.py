"""Intent classifier — multi-cluster K-NN cosine similarity.

Predict intent của 1 câu hỏi bằng cách so với các cluster (mỗi intent 1 cluster):
  - "call_api"      → cluster của API embeddings  (artifacts/api/faiss.index)
  - "call_document" → cluster của doc chunks      (artifacts/docs/faiss.index)

Score mỗi intent = mean cosine của top-K nearest hits trong cluster đó.
Predict = argmax(score) → scale tự nhiên khi thêm intent thứ N+1
(chỉ cần thêm 1 cluster mới vào dict CLUSTERS).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

import numpy as np

import config
from rag.src.indexing.embedder import Embedder
from rag.src.indexing.faiss_store import FaissStore
from shared.types import Question

# Map intent label → đường dẫn FAISS index của cluster đó.
# Thêm intent mới: chỉ cần add entry vào đây.
CLUSTERS: dict[str, Path] = {
    "call_api":      config.API_FAISS,
    "call_document": config.DOC_FAISS,
}


# ──────────────────────────────────────────────────────────────────────────────
# Lazy singletons
# ──────────────────────────────────────────────────────────────────────────────

_embedder: Embedder | None = None
_stores: dict[str, FaissStore] | None = None


def _get_embedder() -> Embedder:
    global _embedder
    if _embedder is None:
        _embedder = Embedder()
    return _embedder


def _get_stores() -> dict[str, FaissStore]:
    """Load FAISS index cho mỗi intent (lazy, cache memory)."""
    global _stores
    if _stores is None:
        _stores = {}
        for label, path in CLUSTERS.items():
            store = FaissStore()
            store.load(path)
            _stores[label] = store
    return _stores


# ──────────────────────────────────────────────────────────────────────────────
# Scoring
# ──────────────────────────────────────────────────────────────────────────────

def _knn_score(query_vec: np.ndarray, store: FaissStore, top_k: int) -> float:
    """Mean cosine của top-K nearest neighbors trong cluster."""
    hits = store.search(query_vec, top_k=top_k)
    if not hits:
        return 0.0
    return sum(h.score for h in hits) / len(hits)


# ──────────────────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────────────────

def predict(question: Question) -> tuple[str, float]:
    """Predict intent + confidence.

    Returns:
        (label, confidence) — confidence = margin giữa winner và runner-up.
        Margin càng lớn càng chắc chắn.

    KHÔNG dùng question.note — đề bài cấm.
    """
    query_vec = _get_embedder().encode_query(question.question)
    top_k = config.INTENT_TOP_K
    scores = {label: _knn_score(query_vec, store, top_k) for label, store in _get_stores().items()}

    sorted_scores = sorted(scores.values(), reverse=True)
    label = max(scores, key=scores.get)
    margin = sorted_scores[0] - sorted_scores[1] if len(sorted_scores) > 1 else sorted_scores[0]
    return label, float(margin)
