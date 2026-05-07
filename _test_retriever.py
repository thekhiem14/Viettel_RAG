"""Test FAISS+BM25+Fuzzy retrieval thật trên 20 câu call_api từ example data.

GT được derive từ `func_param.path` -> schemas.path -> func_code (không hard-code).
"""
import sys
import json
import csv

sys.path.insert(0, ".")
sys.stdout.reconfigure(encoding="utf-8")

import config
from rag.src.retrieval.api_retriever import APIRetriever

# 1. Load schemas -> build path -> func_code map
schemas = json.loads(config.API_SCHEMAS.read_text(encoding="utf-8"))
path_to_code = {s["path"]: fc for fc, s in schemas.items() if s.get("path")}

# 2. Load questions (id -> question)
questions_map: dict[str, str] = {}
with open(config.EXAMPLE_CSV, encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        questions_map[r["id"]] = r["fun_question"]

# 3. Lấy 20 câu call_api đầu có path map được sang func_code
ground_truth: dict[str, str] = {}
sample_ids: list[str] = []
with open(config.EXAMPLE_RESULT_CSV, encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        if r["func_code"] != "call_api":
            continue
        try:
            param = json.loads(r["func_param"])
        except json.JSONDecodeError:
            continue
        path = param.get("path")
        fc = path_to_code.get(path)
        if fc:
            ground_truth[r["id"]] = fc
            sample_ids.append(r["id"])
            if len(sample_ids) >= 20:
                break

print(f"[setup] sampled {len(sample_ids)} call_api questions with mapped GT")

# 4. Run retriever (FAISS + BM25 + Fuzzy)
retriever = APIRetriever()

hit_at_1 = 0
hit_at_5 = 0

print("=" * 70)
for qid in sample_ids:
    question = questions_map[qid]
    gt = ground_truth[qid]
    hits = retriever.search(question, top_k=5)

    rank = next((i + 1 for i, h in enumerate(hits) if h.id == gt), None)
    if rank == 1:
        hit_at_1 += 1
    if rank:
        hit_at_5 += 1

    print(f"\nID {qid}: {question[:90]}")
    print(f"  GT: {gt}")
    for i, h in enumerate(hits):
        marker = " <<<" if h.id == gt else ""
        name = schemas.get(h.id, {}).get("name", "?")
        print(f"    {i+1}. {h.id} ({name[:55]}) score={h.score:.4f}{marker}")
    print(f"  => rank: {rank if rank else 'NOT FOUND'}")

n = len(sample_ids)
print("\n" + "=" * 70)
print(f"Hit@1 = {hit_at_1}/{n} ({hit_at_1/n*100:.1f}%)")
print(f"Hit@5 = {hit_at_5}/{n} ({hit_at_5/n*100:.1f}%)")
