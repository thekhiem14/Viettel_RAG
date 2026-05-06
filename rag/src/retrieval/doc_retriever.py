from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

import config
from rag.src.indexing.bm25_store import BM25Store
from rag.src.indexing.embedder import Embedder
from rag.src.indexing.faiss_store import FaissStore
from rag.src.retrieval.rrf import rrf_fusion
from shared.types import Chunk, RetrievalHit
from shared.utils.io import load_jsonl

_PUBLIC_RE = re.compile(r"Public_\d+")
_embedder: Embedder | None = None
_chunks_map: dict[str, Chunk] | None = None


def _get_embedder() -> Embedder:
    global _embedder
    if _embedder is None:
        _embedder = Embedder()
    return _embedder


def _get_chunks_map() -> dict[str, Chunk]:
    global _chunks_map
    if _chunks_map is None:
        _chunks_map = {
            d["chunk_id"]: Chunk(**d)
            for d in load_jsonl(config.DOC_CHUNKS)
        }
    return _chunks_map


class DocRetriever:
    """Hybrid retriever cho call_document: FAISS + BM25 → RRF → top candidates.

    filter_fn: nếu câu hỏi đề cập Public_XXX thì chỉ search trong doc đó.
    """

    def __init__(self) -> None:
        self._faiss = FaissStore()
        self._faiss.load(config.DOC_FAISS)

        self._bm25 = BM25Store()
        self._bm25.load(config.DOC_BM25)

    def search(
        self,
        query: str,
        top_k: int = 20,
        doc_id: str | None = None,
    ) -> list[Chunk]:
        """Tìm top_k chunks liên quan.

        Args:
            query: câu hỏi
            top_k: số chunks trả về (trước rerank)
            doc_id: nếu có, chỉ lấy chunks thuộc doc này (Public_XXX)

        Returns:
            list[Chunk] đã sort theo RRF score
        """
        embedder = _get_embedder()
        chunks_map = _get_chunks_map()

        filter_fn = (lambda cid: cid.startswith(doc_id)) if doc_id else None

        query_vec = embedder.encode_query(query)
        faiss_hits = self._faiss.search(query_vec, top_k=top_k * 2, filter_fn=filter_fn)
        bm25_hits = self._bm25.search(query, top_k=top_k * 2)

        # BM25 post-filter nếu có doc_id
        if doc_id:
            bm25_hits = [h for h in bm25_hits if h.id.startswith(doc_id)]

        merged = rrf_fusion([faiss_hits, bm25_hits], k=config.RRF_K, top_k=top_k)
        return [chunks_map[h.id] for h in merged if h.id in chunks_map]

    @staticmethod
    def extract_doc_id(question: str) -> str | None:
        """Regex extract Public_XXX từ câu hỏi."""
        m = _PUBLIC_RE.search(question)
        return m.group() if m else None
