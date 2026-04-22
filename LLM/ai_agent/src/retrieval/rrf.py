"""
Reciprocal Rank Fusion — merge vector và BM25 results.
score(d) = Σ 1 / (k + rank_i(d))
"""


def rrf_merge(
    vector_results: list[dict],
    bm25_results: list[dict],
    k: int = 60,
    top_n: int = 20,
) -> list[dict]:
    """
    Nhận 2 ranked lists (vector + BM25), trả về list merged và sorted theo RRF score.
    Mỗi item cần có trường 'chunk_id' và 'full_text'.
    """
    scores: dict[str, float] = {}
    data: dict[str, dict] = {}

    for rank, item in enumerate(vector_results):
        cid = item['chunk_id']
        scores[cid] = scores.get(cid, 0.0) + 1.0 / (k + rank + 1)
        data[cid] = item

    for rank, item in enumerate(bm25_results):
        cid = item['chunk_id']
        scores[cid] = scores.get(cid, 0.0) + 1.0 / (k + rank + 1)
        if cid not in data:
            data[cid] = item

    sorted_ids = sorted(scores, key=lambda cid: scores[cid], reverse=True)[:top_n]

    result = []
    for cid in sorted_ids:
        item = dict(data[cid])
        item['rrf_score'] = scores[cid]
        result.append(item)

    return result
