"""Eval không dùng LLM — đo intent accuracy + API retrieval hit rate.

Metrics:
  - Intent accuracy (cosine classifier vs GT func_code), kèm confidence từng câu
  - API retrieval: Hit@1, Hit@5 — GT = func_code map từ path trong schemas.json
  - Doc: không có retrieval GT (chỉ có đáp án A/B/C/D, không có chunk GT)
    → chỉ log intent confidence để debug

Usage:
    python _eval_no_llm.py
"""
from __future__ import annotations

import csv
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, ".")
sys.stdout.reconfigure(encoding="utf-8")

import config
from intent.src.classifier import predict
from rag.src.indexing.bm25_store import BM25Store
from rag.src.indexing.embedder import Embedder
from rag.src.indexing.faiss_store import FaissStore
from rag.src.retrieval.rrf import rrf_fusion
from shared.types import Question
from shared.utils.io import load_jsonl


# ── Load data ──────────────────────────────────────────────────────────────────

def _load_questions() -> list[Question]:
    questions = []
    with open(config.EXAMPLE_CSV, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            questions.append(Question(id=r["id"], question=r["fun_question"], note=r.get("note")))
    return questions


def _load_gt() -> dict[str, dict]:
    """id → {func_code, path, answer}"""
    schemas = json.loads(config.API_SCHEMAS.read_text(encoding="utf-8"))
    path_to_fc = {s["path"]: fc for fc, s in schemas.items() if s.get("path")}

    gt = {}
    with open(config.EXAMPLE_RESULT_CSV, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            qid = r["id"]
            func_code = r["func_code"]
            func_param_raw = r.get("func_param", "")

            entry: dict = {"func_code": func_code}

            if func_code == "call_api":
                try:
                    param = json.loads(func_param_raw)
                    path = param.get("path", "")
                    entry["path"] = path
                    entry["gt_fc"] = path_to_fc.get(path, "")  # func_code cụ thể từ schemas
                except (json.JSONDecodeError, TypeError):
                    entry["path"] = ""
                    entry["gt_fc"] = ""
            else:
                try:
                    param = json.loads(func_param_raw)
                    entry["answer"] = str(param.get("result", "")).strip().upper()
                except (json.JSONDecodeError, TypeError):
                    entry["answer"] = ""

            gt[qid] = entry
    return gt


def _hits_at_k(ranked: list[str], gt: str, ks: list[int]) -> list[bool]:
    return [gt in ranked[:k] for k in ks]


def _print_table(title: str, n: int, rows: list[tuple[str, list[int]]], ks: list[int]) -> None:
    sep = "=" * 66
    print(f"\n{sep}")
    print(f"  {title} (n={n})")
    print(sep)
    print(f"  {'Strategy':<28}" + "".join(f"Hit@{k:>2}   " for k in ks))
    print("-" * 66)
    for name, counts in rows:
        print(f"  {name:<28}" + "".join(f"{c/n:>6.1%}  " for c in counts))
    print(sep)


# ── Load shared resources ──────────────────────────────────────────────────────

print("[eval_no_llm] Loading resources...")
t_load = time.perf_counter()

questions = _load_questions()
gt_map = _load_gt()

embedder = Embedder()
api_faiss = FaissStore(); api_faiss.load(config.API_FAISS)
api_bm25  = BM25Store();  api_bm25.load(config.API_BM25)

print(f"  Loaded in {time.perf_counter() - t_load:.2f}s — {len(questions)} questions")

q_by_id = {q.id: q for q in questions}


# ── Part 1: Intent accuracy ────────────────────────────────────────────────────

SEP = "=" * 72

print(f"\n{SEP}")
print(f"  INTENT CLASSIFIER")
print(SEP)
print(f"  {'id':<6} {'GT':<16} {'Pred':<16} {'Conf':>6}  {'ms':>6}  OK")
print(f"  {'-'*6} {'-'*16} {'-'*16} {'-'*6}  {'-'*6}  --")

intent_correct = 0
intent_times = []
intent_rows = []

for q in questions:
    gt_code = gt_map.get(q.id, {}).get("func_code", "")
    t0 = time.perf_counter()
    pred_code, conf = predict(q)
    elapsed_ms = (time.perf_counter() - t0) * 1000
    intent_times.append(elapsed_ms)

    ok = pred_code == gt_code
    if ok:
        intent_correct += 1
    intent_rows.append((q.id, gt_code, pred_code, conf, elapsed_ms, ok))
    marker = "✓" if ok else "✗"
    print(f"  {q.id:<6} {gt_code:<16} {pred_code:<16} {conf:>6.3f}  {elapsed_ms:>5.1f}  {marker}")

n_total = len(questions)
n_miss = n_total - intent_correct
print(f"\n  Intent accuracy : {intent_correct/n_total:.1%}  ({intent_correct}/{n_total}, miss={n_miss})")
print(f"  Time — avg: {sum(intent_times)/n_total:.1f}ms  min: {min(intent_times):.1f}ms  max: {max(intent_times):.1f}ms")
if n_miss:
    print(f"\n  Misclassified:")
    for qid, gt_c, pred_c, conf, ms, ok in intent_rows:
        if not ok:
            q = q_by_id[qid]
            print(f"    id={qid}  GT={gt_c}  pred={pred_c}  conf={conf:.3f}  q={q.question[:60]}")


# ── Part 2: API retrieval ──────────────────────────────────────────────────────

TOP_K = 5
ks_api = [1, 5]

api_qs = [(q_by_id[qid], entry)
          for qid, entry in gt_map.items()
          if entry["func_code"] == "call_api" and entry.get("gt_fc") and qid in q_by_id]

n_api = len(api_qs)
n_api_no_gt = sum(1 for qid, entry in gt_map.items()
                  if entry["func_code"] == "call_api" and not entry.get("gt_fc"))

print(f"\n{SEP}")
print(f"  API RETRIEVAL  (n={n_api} có GT, {n_api_no_gt} path không map được trong schemas)")
print(SEP)
print(f"  {'id':<6} {'GT func_code':<36} {'@1':>3} {'@5':>3}  {'ms':>6}")
print(f"  {'-'*6} {'-'*36} {'-'*3} {'-'*3}  {'-'*6}")

api_hits: dict[str, list[int]] = {
    "faiss_only":    [0, 0],
    "bm25_only":     [0, 0],
    "rrf_faiss_bm25":[0, 0],
}
api_ret_times = []

for q, entry in api_qs:
    gt_fc = entry["gt_fc"]
    t0 = time.perf_counter()
    qvec = embedder.encode_query(q.question)
    faiss_hits = api_faiss.search(qvec, top_k=TOP_K * 2)
    bm25_hits  = api_bm25.search(q.question, top_k=TOP_K * 2)
    elapsed_ms = (time.perf_counter() - t0) * 1000
    api_ret_times.append(elapsed_ms)

    rrf_ranked = [h.id for h in rrf_fusion([faiss_hits, bm25_hits], k=config.RRF_K, top_k=TOP_K)]

    strategies = {
        "faiss_only":    [h.id for h in faiss_hits[:TOP_K]],
        "bm25_only":     [h.id for h in bm25_hits[:TOP_K]],
        "rrf_faiss_bm25": rrf_ranked,
    }
    for name, ranked in strategies.items():
        for i, hit in enumerate(_hits_at_k(ranked, gt_fc, ks_api)):
            if hit:
                api_hits[name][i] += 1

    h1 = "✓" if gt_fc in rrf_ranked[:1] else "✗"
    h5 = "✓" if gt_fc in rrf_ranked[:5] else "✗"
    print(f"  {q.id:<6} {gt_fc:<36} {h1:>3} {h5:>3}  {elapsed_ms:>5.1f}")

if n_api_no_gt:
    print(f"\n  Câu API không map được path → func_code:")
    for qid, entry in gt_map.items():
        if entry["func_code"] == "call_api" and not entry.get("gt_fc"):
            q = q_by_id.get(qid)
            print(f"    id={qid}  path={entry.get('path', '?')}  q={q.question[:55] if q else '?'}")

print(f"\n  Time — avg: {sum(api_ret_times)/n_api:.1f}ms  min: {min(api_ret_times):.1f}ms  max: {max(api_ret_times):.1f}ms")
_print_table("API RETRIEVAL SUMMARY", n_api, list(api_hits.items()), ks_api)


# ── Part 3: Doc — intent confidence log ───────────────────────────────────────

doc_qs = [(q_by_id[qid], entry)
          for qid, entry in gt_map.items()
          if entry["func_code"] == "call_document"]

n_doc = len(doc_qs)

print(f"\n{SEP}")
print(f"  DOC QUESTIONS — intent confidence (n={n_doc})")
print(f"  (retrieval GT = chunk/doc_id không có trong CSV → chỉ log intent)")
print(SEP)
print(f"  {'id':<6} {'GT ans':>6}  {'Pred intent':<16} {'Conf':>6}  note_len")
print(f"  {'-'*6} {'-'*6}  {'-'*16} {'-'*6}  --------")

for q, entry in doc_qs:
    gt_ans = entry.get("answer", "?")
    _, conf = predict(q)
    note_len = len(q.note) if q.note else 0
    print(f"  {q.id:<6} {gt_ans:>6}  {'call_document':<16} {conf:>6.3f}  {note_len}")


# ── Summary ────────────────────────────────────────────────────────────────────

print(f"\n{SEP}")
print(f"  SUMMARY")
print(SEP)
print(f"  Total          : {n_total}  (API={n_api}+{n_api_no_gt}_no_gt, Doc={n_doc})")
print(f"  Intent accuracy: {intent_correct/n_total:.1%}  ({intent_correct}/{n_total})")
if n_api:
    h1 = api_hits['rrf_faiss_bm25'][0]
    h5 = api_hits['rrf_faiss_bm25'][1]
    print(f"  API rrf Hit@1  : {h1/n_api:.1%}  ({h1}/{n_api})")
    print(f"  API rrf Hit@5  : {h5/n_api:.1%}  ({h5}/{n_api})")
print(f"{SEP}\n")
