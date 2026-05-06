from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

import config
from rag.src.indexing.bm25_store import BM25Store
from rag.src.indexing.embedder import Embedder
from rag.src.indexing.faiss_store import FaissStore
from rag.src.indexing.fuzzy_store import FuzzyStore
from rag.src.retrieval.rrf import rrf_fusion
from shared.types import RetrievalHit

_embedder: Embedder | None = None


def _get_embedder() -> Embedder:
    global _embedder
    if _embedder is None:
        _embedder = Embedder()
    return _embedder


class APIRetriever:
    """Hybrid retriever cho call_api: FAISS + BM25 + Fuzzy → RRF → top-5."""

    def __init__(self) -> None:
        self._faiss = FaissStore()
        self._faiss.load(config.API_FAISS)

        self._bm25 = BM25Store()
        self._bm25.load(config.API_BM25)

        self._fuzzy = FuzzyStore()
        self._fuzzy.load(config.API_FUZZY)

    def search(self, query: str, top_k: int = config.API_RETRIEVE_TOP_K) -> list[RetrievalHit]:
        """Tìm top_k API candidates bằng hybrid retrieval.

        Chạy 3 nguồn rồi RRF fusion:
          - FAISS: semantic (bge-m3 embedding)
          - BM25: lexical (pyvi segment)
          - Fuzzy: partial string match trên name+description tiếng Việt
        """
        embedder = _get_embedder()
        query_vec = embedder.encode_query(query)

        faiss_hits = self._faiss.search(query_vec, top_k=top_k * 2)
        bm25_hits = self._bm25.search(query, top_k=top_k * 2)
        fuzzy_hits = self._fuzzy.search(query, top_k=top_k * 2)

        return rrf_fusion(
            [faiss_hits, bm25_hits, fuzzy_hits],
            k=config.RRF_K,
            top_k=top_k,
        )
