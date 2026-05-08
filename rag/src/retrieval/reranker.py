from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

import config
from shared.types import Chunk

_reranker = None


def _get_reranker():
    global _reranker

    if _reranker is None:
        from FlagEmbedding import FlagReranker

        _reranker = FlagReranker(
            config.RERANK_MODEL,
            use_fp16=True,
        )

    return _reranker


def rerank(
    query: str,
    chunks: list[Chunk],
    top_k: int = 5,
) -> list[Chunk]:
    """Cross-encoder rerank: trả về top_k chunks theo relevance score."""

    if not chunks:
        return []

    reranker = _get_reranker()

    pairs = [[query, c.text] for c in chunks]

    scores = reranker.compute_score(
        pairs,
        normalize=True,
    )

    # FlagEmbedding:
    # - nhiều pairs  -> list[float]
    # - 1 pair       -> numpy.float64
    scores = np.atleast_1d(scores).astype(float).tolist()

    ranked = sorted(
        zip(scores, chunks),
        key=lambda x: x[0],
        reverse=True,
    )

    return [chunk for _, chunk in ranked[:top_k]]