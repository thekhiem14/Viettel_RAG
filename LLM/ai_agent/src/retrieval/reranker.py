from FlagEmbedding import FlagReranker


RERANKER_MODEL = "BAAI/bge-reranker-v2-m3"


class Reranker:
    def __init__(self, model_name: str = RERANKER_MODEL):
        print(f"Đang load reranker: {model_name}")
        self.reranker = FlagReranker(model_name, use_fp16=True)

    def rerank(self, query: str, candidates: list[dict], top_k: int = 5) -> list[dict]:
        """
        Nhận query + list candidates (mỗi item có 'full_text').
        Trả về top_k items đã rerank, bổ sung trường 'rerank_score'.
        """
        if not candidates:
            return []

        pairs = [[query, c['full_text']] for c in candidates]
        scores = self.reranker.compute_score(pairs, normalize=True)

        if not isinstance(scores, list):
            scores = [scores]

        for item, score in zip(candidates, scores):
            item['rerank_score'] = float(score)

        ranked = sorted(candidates, key=lambda x: x['rerank_score'], reverse=True)
        return ranked[:top_k]
