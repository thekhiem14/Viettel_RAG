from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
import config
from shared.types import Chunk, RetrievalHit

_reranker = None


def _get_reranker():
    global _reranker
    if _reranker is None:
        from FlagEmbedding import FlagReranker
        _reranker = FlagReranker(config.RERANK_MODEL, use_fp16=True)
    return _reranker


def rerank(query: str, chunks: list[Chunk], top_k: int = 5) -> list[Chunk]:
    """Cross-encoder rerank: trả về top_k chunks theo relevance score.

    Args:
        query: câu hỏi user
        chunks: ứng viên từ hybrid retrieval (thường 20)
        top_k: số chunk giữ lại sau rerank

    Returns:
        list[Chunk] sorted by score descending, length <= top_k
    """
    reranker = _get_reranker()
    pairs = [[query, c.text] for c in chunks]
    scores = reranker.compute_score(pairs, normalize=True)

    ranked = sorted(zip(scores, chunks), key=lambda x: x[0], reverse=True)
    return [c for _, c in ranked[:top_k]]
