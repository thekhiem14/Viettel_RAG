import pickle
from typing import Optional
import numpy as np


class BM25Store:
    def __init__(self, bm25_pkl_path: str):
        with open(bm25_pkl_path, 'rb') as f:
            payload = pickle.load(f)

        self.bm25 = payload['bm25']
        self.raw_texts = payload['raw_texts']
        self.metadata = payload['metadata']  # list of {doc_id, heading_path, chunk_id}
        print(f"BM25Store loaded: {len(self.raw_texts)} docs")

    def search(self, query: str, k: int = 20, doc_id: Optional[str] = None) -> list[dict]:
        """
        Trả về list of {chunk_id, doc_id, heading_path, full_text, bm25_score}.
        Nếu doc_id được cung cấp, chỉ tính score cho docs thuộc doc đó.
        """
        tokenized_query = query.split()
        scores = self.bm25.get_scores(tokenized_query)

        if doc_id:
            # Zero-out scores cho docs không thuộc doc_id
            mask = np.array([
                1.0 if m.get('doc_id') == doc_id else 0.0
                for m in self.metadata
            ])
            scores = scores * mask

        top_indices = np.argsort(scores)[::-1][:k]

        output = []
        for idx in top_indices:
            if scores[idx] <= 0:
                continue
            meta = self.metadata[idx]
            output.append({
                'chunk_id': meta.get('chunk_id', ''),
                'doc_id': meta.get('doc_id', ''),
                'heading_path': meta.get('heading_path', ''),
                'full_text': self.raw_texts[idx],
                'bm25_score': float(scores[idx]),
            })

        return output
