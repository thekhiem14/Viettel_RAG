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


# Mỗi intent = 1 kho vector riêng
INTENT_STORES = {
    "call_api":      "artifacts/api/faiss.index",
    "call_document": "artifacts/doc/faiss.index",
    # thêm intent mới chỉ cần thêm dòng này:
    "call_database": "artifacts/db/faiss.index",
}

def predict(question: Question) -> tuple[str, float]:
    query_vec = _get_embedder().encode_query(question.question)
    
    # best_intent = None
    best_intent = "call_document"
    best_score  = -1.0

    for intent, index_path in INTENT_STORES.items():
        if not Path(index_path).exists():
            continue
        store = FaissStore()
        store.load(Path(index_path))
        hits  = store.search(query_vec, top_k=3)
        if not hits:
            continue
        
        # Lấy điểm trung bình top-3 của kho này
        score = sum(h.score for h in hits[:3]) / 3
        
        if score > best_score:
            best_score  = score
            best_intent = intent

    # # Nếu điểm cao nhất vẫn thấp → không chắc
    # if best_score < config.INTENT_LOW_THRESHOLD:
    #     return "unknown", best_score

    return best_intent, best_score
