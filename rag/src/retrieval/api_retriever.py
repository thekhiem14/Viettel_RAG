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
from rag.src.indexing.fuzzy_store import FuzzyStore
from rag.src.retrieval.rrf import rrf_fusion
from shared.types import RetrievalHit

_embedder: Embedder | None = None
_org_alias_map: dict[str, str] | None = None


def _get_embedder() -> Embedder:
    global _embedder
    if _embedder is None:
        _embedder = Embedder()
    return _embedder


def _get_org_alias_map() -> dict[str, str]:
    """Load organization list → {ABBREVIATION: full_name} for query expansion.

    Bảng `organization`: key = tên đầy đủ, value = viết tắt (TTPMVT, TTPMQT...).
    Đảo chiều: value.upper() → key để expand "TTPMVT" → "Trung tâm phần mềm viễn thông".
    """
    global _org_alias_map
    if _org_alias_map is not None:
        return _org_alias_map
    _org_alias_map = {}
    try:
        with open(config.API_ALIASES, encoding="utf-8") as f:
            aliases: dict = json.load(f)
        for entry in aliases.get("organization", []):
            full_name = str(entry.get("key", "")).strip()
            abbrev = str(entry.get("value", "")).strip()
            if full_name and abbrev:
                _org_alias_map[abbrev.upper()] = full_name
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return _org_alias_map


def _expand_query(query: str) -> str:
    """Thay thế từ viết tắt tên trung tâm trong query bằng tên đầy đủ.

    Ví dụ: "doanh thu TTPMVT năm 2024" → "doanh thu Trung tâm phần mềm viễn thông năm 2024"
    Chỉ expand token toàn chữ in hoa ASCII (từ viết tắt), không ảnh hưởng tiếng Việt thường.
    """
    alias_map = _get_org_alias_map()
    if not alias_map:
        return query

    def replace_token(m: re.Match) -> str:
        token = m.group(0)
        expanded = alias_map.get(token)  # alias_map keys already uppercased
        return expanded if expanded else token

    return re.sub(r"\b[A-Z][A-Z0-9]{1,}\b", replace_token, query)


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
          - FAISS: semantic (bge-m3 embedding, dùng query gốc)
          - BM25: lexical (pyvi segment, dùng query đã expand từ viết tắt)
          - Fuzzy: partial string match (dùng query đã expand)
        """
        embedder = _get_embedder()
        query_vec = embedder.encode_query(query)
        expanded_query = _expand_query(query)

        faiss_hits = self._faiss.search(query_vec, top_k=top_k * 2)
        bm25_hits = self._bm25.search(expanded_query, top_k=top_k * 2)
        fuzzy_hits = self._fuzzy.search(expanded_query, top_k=top_k * 2)

        return rrf_fusion(
            [faiss_hits, bm25_hits, fuzzy_hits],
            k=config.RRF_K,
            top_k=top_k,
        )
