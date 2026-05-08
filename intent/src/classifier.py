"""Intent classifier dùng cosine similarity giữa query embedding và 131 API embeddings.

Đề bài cấm dùng `note` để phân loại intent — chỉ được dùng `id` và `question`.
Nguồn vector: artifacts/api/faiss.index (131 × 1024-dim, L2-normalized, bge-m3).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

import config
from rag.src.indexing.embedder import Embedder
from rag.src.indexing.faiss_store import FaissStore
from shared.types import Question

_embedder: Embedder | None = None
_faiss: FaissStore | None = None


def _get_embedder() -> Embedder:
    global _embedder
    if _embedder is None:
        _embedder = Embedder()
    return _embedder


def _get_faiss() -> FaissStore:
    global _faiss
    if _faiss is None:
        store = FaissStore()
        store.load(config.API_FAISS)
        _faiss = store
    return _faiss


def predict(question: Question) -> tuple[str, float]:
    """Predict intent: 'call_api' nếu cosine sim cao, 'call_document' nếu thấp.

    KHÔNG dùng question.note — đề bài cấm.
    """
    embedder = _get_embedder()
    faiss = _get_faiss()

    query_vec = embedder.encode_query(question.question)
    hits = faiss.search(query_vec, top_k=1)

    sim = hits[0].score if hits else 0.0

    if sim >= config.INTENT_COSINE_THRESHOLD:
        return "call_api", sim
    return "call_document", 1.0 - sim
