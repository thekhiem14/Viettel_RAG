from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
from shared.types import RetrievalHit


def rrf_fusion(
    results_per_source: list[list[RetrievalHit]],
    k: int = 60,
    top_k: int = 5,
) -> list[RetrievalHit]:
    """Reciprocal Rank Fusion over multiple retrieval result lists.

    score(d) = Σ 1 / (k + rank_i(d))

    Args:
        results_per_source: each inner list is top-N hits from one source (bm25/faiss/fuzzy)
        k: RRF constant (60 is standard default)
        top_k: number of results to return

    Returns:
        Merged list of RetrievalHit sorted by fused score, length <= top_k.
        source field is set to "rrf", score is the fused score.
    """
    scores: dict[str, float] = {}

    for hits in results_per_source:
        for hit in hits:
            scores[hit.id] = scores.get(hit.id, 0.0) + 1.0 / (k + hit.rank)

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_k]

    return [
        RetrievalHit(id=hit_id, score=score, source="rrf", rank=rank)
        for rank, (hit_id, score) in enumerate(ranked)
    ]
