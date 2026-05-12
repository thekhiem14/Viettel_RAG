"""Eval pipeline trên 100 example questions với ground truth comparison.

Metrics:
  - Intent accuracy (predicted vs GT func_code)
  - call_api: JSON validity, func_code match, path match
  - call_document: answer format valid (A/B/C/D), exact answer match
  - Avg time_response

Usage:
    python rag/scripts/06_eval.py

Output:
    outputs/eval/predictions.jsonl
    outputs/eval/metrics.json
"""
from __future__ import annotations

import csv
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import config
from intent.src.md_parser import parse_example_csv
from rag.src.pipeline.orchestrator import run_batch
from shared.utils.io import save_json, save_jsonl
from shared.utils.logger import get_logger

logger = get_logger("06_eval", config.LOGS_DIR)

_ANS_RE = re.compile(r"^[A-D]{1,4}$")


def _load_ground_truth() -> dict[str, dict]:
    """Load example_data_example_result.csv → {id: {func_code, func_param}}."""
    gt: dict[str, dict] = {}
    with open(config.EXAMPLE_RESULT_CSV, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            qid = row.get("id", "").strip()
            if qid:
                gt[qid] = {
                    "func_code": row.get("func_code", "").strip(),
                    "func_param": row.get("func_param", "").strip(),
                }
    return gt


def _build_path_to_fc() -> dict[str, str]:
    """path → func_code từ schemas.json."""
    schemas = json.loads(config.API_SCHEMAS.read_text(encoding="utf-8"))
    return {s["path"]: fc for fc, s in schemas.items() if s.get("path")}


def _parse_answer(func_param_gt: str) -> str:
    """Extract đáp án A/B/C/D từ GT func_param JSON (field 'result')."""
    try:
        parsed = json.loads(func_param_gt)
        return str(parsed.get("result", "")).strip().upper()
    except Exception:
        return ""


def _parse_api_gt(func_param_gt: str, path_to_fc: dict[str, str]) -> dict:
    """Parse GT func_param → {func_code, path}. func_code lấy qua path→schemas mapping."""
    try:
        parsed = json.loads(func_param_gt)
        path = parsed.get("path", "")
        return {"func_code": path_to_fc.get(path, ""), "path": path}
    except Exception:
        return {"func_code": "", "path": ""}


def main() -> None:
    config.ensure_dirs()

    questions = parse_example_csv(config.EXAMPLE_CSV)
    if not questions:
        raise RuntimeError(f"No questions parsed from {config.EXAMPLE_CSV}")

    gt = _load_ground_truth()
    path_to_fc = _build_path_to_fc()

    print(f"[06_eval] running on {len(questions)} questions...")
    t0 = time.perf_counter()
    results = run_batch(questions)
    total_time = time.perf_counter() - t0

    # Save raw predictions
    out_pred = config.OUTPUTS_DIR / "eval" / "predictions.jsonl"
    save_jsonl(out_pred, results)

    # ── Compute metrics ──────────────────────────────────────────────────────
    intent_correct = 0
    api_results, doc_results = [], []
    api_json_valid = api_code_match = api_path_match = 0
    doc_format_valid = doc_answer_match = 0

    for r in results:
        qid = str(r["id"])
        pred_code = r["function_code"]
        gt_entry = gt.get(qid, {})
        gt_code = gt_entry.get("func_code", "")
        gt_param = gt_entry.get("func_param", "")

        if pred_code == gt_code:
            intent_correct += 1

        if pred_code == "call_api":
            api_results.append(r)
            try:
                pred = json.loads(r["function_result"])
                has_fields = "func_code" in pred and "path" in pred and "body" in pred
                if has_fields:
                    api_json_valid += 1
                gt_api = _parse_api_gt(gt_param, path_to_fc)
                if pred.get("func_code") == gt_api.get("func_code"):
                    api_code_match += 1
                if pred.get("path") == gt_api.get("path"):
                    api_path_match += 1
            except Exception:
                pass

        else:  # call_document
            doc_results.append(r)
            ans = r["function_result"].strip()
            if _ANS_RE.match(ans):
                doc_format_valid += 1
            gt_ans = _parse_answer(gt_param)
            if gt_ans and ans == gt_ans:
                doc_answer_match += 1

    n = len(results)
    n_api = len(api_results) or 1
    n_doc = len(doc_results) or 1

    metrics = {
        "total": n,
        "api_count": len(api_results),
        "doc_count": len(doc_results),
        # intent
        "intent_accuracy": round(intent_correct / n, 4),
        # api
        "api_json_valid_rate": round(api_json_valid / n_api, 4),
        "api_func_code_match_rate": round(api_code_match / n_api, 4),
        "api_path_match_rate": round(api_path_match / n_api, 4),
        # doc
        "doc_format_valid_rate": round(doc_format_valid / n_doc, 4),
        "doc_answer_match_rate": round(doc_answer_match / n_doc, 4),
        # time
        "avg_time_response": round(sum(r["time_response"] for r in results) / n, 4),
        "total_wall_time": round(total_time, 2),
    }

    out_metrics = config.OUTPUTS_DIR / "eval" / "metrics.json"
    save_json(out_metrics, metrics)

    # ── Print summary ────────────────────────────────────────────────────────
    print(f"\n[06_eval] DONE — {n} questions in {total_time:.1f}s")
    print(f"  Intent accuracy:      {metrics['intent_accuracy']:.1%}  ({intent_correct}/{n})")
    print(f"  API JSON valid:       {metrics['api_json_valid_rate']:.1%}  ({api_json_valid}/{len(api_results)})")
    print(f"  API func_code match:  {metrics['api_func_code_match_rate']:.1%}  ({api_code_match}/{len(api_results)})")
    print(f"  API path match:       {metrics['api_path_match_rate']:.1%}  ({api_path_match}/{len(api_results)})")
    print(f"  Doc format valid:     {metrics['doc_format_valid_rate']:.1%}  ({doc_format_valid}/{len(doc_results)})")
    print(f"  Doc answer match:     {metrics['doc_answer_match_rate']:.1%}  ({doc_answer_match}/{len(doc_results)})")
    print(f"  Avg time_response:    {metrics['avg_time_response']:.2f}s  (target <{config.TIME_RESPONSE_TARGET}s)")
    print(f"  Saved -> {out_pred}")
    print(f"  Saved -> {out_metrics}")

    if metrics["intent_accuracy"] < 0.95:
        print(f"\n  !! Intent accuracy < 95% — check INTENT_COSINE_THRESHOLD (hiện: {config.INTENT_COSINE_THRESHOLD})")
    if metrics["avg_time_response"] > config.TIME_RESPONSE_TARGET:
        print(f"  !! avg time > {config.TIME_RESPONSE_TARGET}s — cần optimize")


if __name__ == "__main__":
    main()
