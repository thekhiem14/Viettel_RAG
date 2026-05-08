"""Retrieval benchmark — so sánh các chiến lược retrieval, không dùng LLM.

Đo Hit@K cho từng strategy: FAISS only, BM25 only, RRF combinations.
Chạy trên call_api + call_document từ example data.

Usage:
    python _test_retrieval_benchmark.py

Không cần GPU. Chỉ cần bge-m3 để encode query (CPU OK, chậm hơn).
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, ".")
sys.stdout.reconfigure(encoding="utf-8")

import config
from rag.src.indexing.bm25_store import BM25Store
from rag.src.indexing.embedder import Embedder
from rag.src.indexing.faiss_store import FaissStore
from rag.src.retrieval.api_retriever import APIRetriever
from rag.src.retrieval.doc_retriever import DocRetriever
from rag.src.retrieval.rrf import rrf_fusion
from shared.utils.io import load_jsonl

TOP_K = 5
DOC_TOP_K = 20


# ── Helpers ──────────────────────────────────────────────────────────────────

def _load_questions() -> dict[str, str]:
    """id → question text"""
    out = {}
    with open(config.EXAMPLE_CSV, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            out[r["id"]] = r["fun_question"]
    return out


def _load_ground_truth() -> tuple[dict[str, str], dict[str, str]]:
    """Returns (api_gt, doc_gt) where:
    - api_gt: {id: func_code}  derived from func_param.path → schemas.path
    - doc_gt: {id: doc_id}     derived from Public_XXX in question text
    """
    schemas = json.loads(config.API_SCHEMAS.read_text(encoding="utf-8"))
    path_to_code = {s["path"]: fc for fc, s in schemas.items() if s.get("path")}

    api_gt: dict[str, str] = {}
    doc_gt_ids: list[str] = []  # ids that are call_document

    with open(config.EXAMPLE_RESULT_CSV, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            qid = r["id"]
            if r["func_code"] == "call_api":
                try:
                    param = json.loads(r["func_param"])
                    fc = path_to_code.get(param.get("path", ""))
                    if fc:
                        api_gt[qid] = fc
                except (json.JSONDecodeError, TypeError):
                    pass
            elif r["func_code"] == "call_document":
                doc_gt_ids.append(qid)

    return api_gt, doc_gt_ids


def _hits_at_k(ranked_ids: list[str], gt_id: str, ks: list[int]) -> list[bool]:
    """Check if gt_id appears in top-k for each k."""
    return [gt_id in ranked_ids[:k] for k in ks]


def _print_table(title: str, n: int, strategies: list[tuple[str, list[int], list[int]]], ks: list[int]) -> None:
    """strategies = list of (name, hit_at_k_counts...)"""
    sep = "=" * 62
    print(f"\n{sep}")
    print(f"  {title} (n={n})")
    print(sep)
    header = f"  {'Strategy':<28}" + "".join(f"Hit@{k:>2}   " for k in ks)
    print(header)
    print("-" * 62)
    for name, counts in strategies:
        row = f"  {name:<28}" + "".join(f"{c/n:>6.1%}  " for c in counts)
        print(row)
    print(sep)


# ── Load shared resources ─────────────────────────────────────────────────────

print("[benchmark] Loading shared resources...")

questions_map = _load_questions()
api_gt, doc_gt_ids = _load_ground_truth()

embedder = Embedder()
print(f"  Embedder ready")

# API indices
api_faiss = FaissStore(); api_faiss.load(config.API_FAISS)
api_bm25  = BM25Store();  api_bm25.load(config.API_BM25)
api_retriever = APIRetriever()  # rrf_faiss_bm25 (with query expansion)
print(f"  API indices ready ({len(api_gt)} GT entries)")

# DOC indices
doc_faiss = FaissStore(); doc_faiss.load(config.DOC_FAISS)
doc_bm25  = BM25Store();  doc_bm25.load(config.DOC_BM25)
chunks_map = {d["chunk_id"]: d["doc_id"] for d in load_jsonl(config.DOC_CHUNKS)}
print(f"  Doc indices ready ({len(chunks_map)} chunks)")


# ── Part 1: API Retrieval Benchmark ──────────────────────────────────────────

print("\n[benchmark] Running API strategies...")

api_ids = list(api_gt.keys())
n_api = len(api_ids)
ks_api = [1, 5]

# Accumulators: {strategy_name: [hit@1_count, hit@5_count]}
api_hits: dict[str, list[int]] = {
    "faiss_only":    [0, 0],
    "bm25_only":     [0, 0],
    "rrf_faiss_bm25":[0, 0],
    "rrf_all":       [0, 0],
}

for qid in api_ids:
    query = questions_map[qid]
    gt_fc = api_gt[qid]
    qvec  = embedder.encode_query(query)

    faiss_hits = api_faiss.search(qvec, top_k=TOP_K * 2)
    bm25_hits  = api_bm25.search(query, top_k=TOP_K * 2)

    strategies_results = {
        "faiss_only":     [h.id for h in faiss_hits[:TOP_K]],
        "bm25_only":      [h.id for h in bm25_hits[:TOP_K]],
        "rrf_faiss_bm25": [h.id for h in rrf_fusion([faiss_hits, bm25_hits], k=config.RRF_K, top_k=TOP_K)],
        "rrf_all":        [h.id for h in api_retriever.search(query, top_k=TOP_K)],
    }

    for name, ranked in strategies_results.items():
        hits = _hits_at_k(ranked, gt_fc, ks_api)
        for i, hit in enumerate(hits):
            if hit:
                api_hits[name][i] += 1

_print_table(
    "API RETRIEVAL BENCHMARK",
    n_api,
    [(name, counts) for name, counts in api_hits.items()],
    ks_api,
)


# ── Part 2: Doc Retrieval Benchmark ──────────────────────────────────────────

print("\n[benchmark] Running Doc strategies...")

# GT: Public_XXX từ question text
doc_ids_with_gt: list[tuple[str, str]] = []  # (qid, gt_doc_id)
for qid in doc_gt_ids:
    q = questions_map.get(qid, "")
    doc_id = DocRetriever.extract_doc_id(q)
    if doc_id:
        doc_ids_with_gt.append((qid, doc_id))

n_doc = len(doc_ids_with_gt)
ks_doc = [1, 5, 20]

doc_hits: dict[str, list[int]] = {
    "faiss_only":       [0, 0, 0],
    "bm25_only":        [0, 0, 0],
    "rrf_faiss_bm25":   [0, 0, 0],
    "faiss_with_filter":[0, 0, 0],
    "rrf_with_filter":  [0, 0, 0],
}

for qid, gt_doc_id in doc_ids_with_gt:
    query  = questions_map[qid]
    qvec   = embedder.encode_query(query)
    filter_fn = lambda cid: cid.startswith(gt_doc_id)

    faiss_raw  = doc_faiss.search(qvec, top_k=DOC_TOP_K * 2)
    bm25_raw   = doc_bm25.search(query, top_k=DOC_TOP_K * 2)
    faiss_filt = doc_faiss.search(qvec, top_k=DOC_TOP_K * 2, filter_fn=filter_fn)

    def chunk_to_doc(hit_id: str) -> str:
        return chunks_map.get(hit_id, "")

    strategies_results = {
        "faiss_only":       [chunk_to_doc(h.id) for h in faiss_raw[:DOC_TOP_K]],
        "bm25_only":        [chunk_to_doc(h.id) for h in bm25_raw[:DOC_TOP_K]],
        "rrf_faiss_bm25":   [chunk_to_doc(h.id) for h in rrf_fusion([faiss_raw, bm25_raw], k=config.RRF_K, top_k=DOC_TOP_K)],
        "faiss_with_filter":[chunk_to_doc(h.id) for h in faiss_filt[:DOC_TOP_K]],
        "rrf_with_filter":  [chunk_to_doc(h.id) for h in rrf_fusion(
                                [doc_faiss.search(qvec, top_k=DOC_TOP_K * 2, filter_fn=filter_fn),
                                 [h for h in bm25_raw if h.id.startswith(gt_doc_id)]],
                                k=config.RRF_K, top_k=DOC_TOP_K)],
    }

    for name, doc_ids_ranked in strategies_results.items():
        hits = _hits_at_k(doc_ids_ranked, gt_doc_id, ks_doc)
        for i, hit in enumerate(hits):
            if hit:
                doc_hits[name][i] += 1

if n_doc > 0:
    _print_table(
        f"DOC RETRIEVAL BENCHMARK (GT=Public_XXX in question)",
        n_doc,
        [(name, counts) for name, counts in doc_hits.items()],
        ks_doc,
    )
else:
    print("\n[benchmark] No doc questions with extractable Public_XXX GT — skip doc benchmark")

print(f"\n[benchmark] Done. API={n_api} câu, Doc={n_doc} câu với GT.\n")
