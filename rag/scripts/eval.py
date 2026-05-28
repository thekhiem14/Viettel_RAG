"""Eval pipeline trên 100 example questions với ground truth comparison.

Metrics:
  - Intent accuracy (predicted vs GT func_code)
  - call_api: JSON validity, func_code match, path match, per-param accuracy
  - call_document: answer format valid (A/B/C/D), exact answer match
  - Avg time_response

Usage:
    python rag/scripts/06_eval.py

Output:
    outputs/eval/predictions.jsonl
    outputs/eval/metrics.json
    outputs/eval/api_param_errors.csv  (per-question param diff)
"""
from __future__ import annotations

import csv
import json
import re
import sys
import time
from collections import Counter
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
    """Parse GT func_param → {func_code, path, body}. func_code lấy qua path→schemas mapping."""
    try:
        parsed = json.loads(func_param_gt)
        path = parsed.get("path", "")
        body = parsed.get("body", {})
        if isinstance(body, str):
            try:
                body = json.loads(body)
            except Exception:
                body = {}
        return {"func_code": path_to_fc.get(path, ""), "path": path, "body": body if isinstance(body, dict) else {}}
    except Exception:
        return {"func_code": "", "path": "", "body": {}}


def _norm_value(v):
    """Chuẩn hóa value để so sánh: list sort, string strip lower, None/[]/'' coi như rỗng."""
    if v is None or v == "" or v == []:
        return None
    if isinstance(v, list):
        return tuple(sorted(str(x).strip().lower() for x in v))
    if isinstance(v, str):
        return v.strip().lower()
    return v


def _diff_body(pred_body: dict, gt_body: dict) -> dict:
    """So sánh từng param trong body. Returns:
        {
          "missing":  list[str]  — key có trong GT, không có trong pred (hoặc giá trị rỗng)
          "extra":    list[str]  — key có trong pred, không có trong GT
          "wrong":    list[(key, pred_val, gt_val)] — giá trị khác
          "correct":  list[str]
        }
    """
    missing, extra, wrong, correct = [], [], [], []
    gt_keys = set(gt_body.keys())
    pred_keys = set(pred_body.keys())

    for k in gt_keys:
        gt_v = _norm_value(gt_body.get(k))
        pred_v = _norm_value(pred_body.get(k))
        if k not in pred_keys or pred_v is None:
            if gt_v is not None:  # GT có giá trị thật → coi là missing
                missing.append(k)
            else:
                correct.append(k)  # cả 2 đều rỗng
        elif pred_v == gt_v:
            correct.append(k)
        else:
            wrong.append((k, pred_body.get(k), gt_body.get(k)))

    for k in pred_keys - gt_keys:
        if _norm_value(pred_body.get(k)) is not None:
            extra.append(k)

    return {"missing": missing, "extra": extra, "wrong": wrong, "correct": correct}


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

    # Per-param tracking
    missing_counter: Counter = Counter()
    extra_counter: Counter = Counter()
    wrong_counter: Counter = Counter()
    param_total_correct = 0
    param_total = 0
    api_param_rows: list[dict] = []

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
                has_fields = "path" in pred and "body" in pred
                if has_fields:
                    api_json_valid += 1
                gt_api = _parse_api_gt(gt_param, path_to_fc)
                pred_fc = pred.get("func_code") or path_to_fc.get(pred.get("path", ""), "")
                if pred_fc == gt_api.get("func_code"):
                    api_code_match += 1
                if pred.get("path") == gt_api.get("path"):
                    api_path_match += 1

                # Param-level diff (chỉ chấm khi path đúng, không thì meaningless)
                if pred.get("path") == gt_api.get("path"):
                    pred_body = pred.get("body", {}) or {}
                    gt_body = gt_api.get("body", {}) or {}
                    diff = _diff_body(pred_body, gt_body)
                    for k in diff["missing"]:
                        missing_counter[k] += 1
                    for k in diff["extra"]:
                        extra_counter[k] += 1
                    for k, _, _ in diff["wrong"]:
                        wrong_counter[k] += 1
                    n_gt = len(diff["correct"]) + len(diff["missing"]) + len(diff["wrong"])
                    param_total += n_gt
                    param_total_correct += len(diff["correct"])
                    api_param_rows.append({
                        "id": qid,
                        "path": pred.get("path", ""),
                        "missing": ",".join(diff["missing"]),
                        "extra": ",".join(diff["extra"]),
                        "wrong": "; ".join(f"{k}={pv!r}→{gv!r}" for k, pv, gv in diff["wrong"]),
                        "n_correct": len(diff["correct"]),
                        "n_total": n_gt,
                    })
            except Exception as e:
                logger.warning("api_eval_parse_failed", extra={"id": qid, "err": str(e)})

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
        "api_param_accuracy": round(param_total_correct / param_total, 4) if param_total else 0.0,
        "api_param_total": param_total,
        "api_param_correct": param_total_correct,
        "api_top_missing": missing_counter.most_common(15),
        "api_top_extra": extra_counter.most_common(15),
        "api_top_wrong": wrong_counter.most_common(15),
        # doc
        "doc_format_valid_rate": round(doc_format_valid / n_doc, 4),
        "doc_answer_match_rate": round(doc_answer_match / n_doc, 4),
        # time
        "avg_time_response": round(sum(r["time_response"] for r in results) / n, 4),
        "total_wall_time": round(total_time, 2),
    }

    out_metrics = config.OUTPUTS_DIR / "eval" / "metrics.json"
    save_json(out_metrics, metrics)

    # ── Save per-question API param diff ─────────────────────────────────────
    out_api_diff = config.OUTPUTS_DIR / "eval" / "api_param_errors.csv"
    with open(out_api_diff, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "path", "n_correct", "n_total", "missing", "extra", "wrong"],
                                 quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in api_param_rows:
            writer.writerow(row)

    # ── Save submission_eval.csv ─────────────────────────────────────────────
    out_eval = config.OUTPUTS_DIR / "eval" / "submission_eval.csv"
    with open(out_eval, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["id", "func_code", "raw_result", "func_param_formatted", "time"])
        for r in results:
            func_code = r["function_code"]
            processed = r["function_result"]
            raw = r.get("raw_llm", "")
            if func_code == "call_document":
                letters = [c for c in processed.upper() if c in "ABCD"]
                formatted = json.dumps({"numbers": len(letters), "result": ",".join(letters)}, ensure_ascii=False)
            else:
                try:
                    obj = json.loads(processed)
                    formatted = json.dumps({"path": obj.get("path", ""), "body": obj.get("body", {})}, ensure_ascii=False)
                except Exception:
                    formatted = processed
            writer.writerow([r["id"], func_code, raw, formatted, r["time_response"]])

    # ── Print summary ────────────────────────────────────────────────────────
    print(f"\n[06_eval] DONE — {n} questions in {total_time:.1f}s")
    print(f"  Intent accuracy:      {metrics['intent_accuracy']:.1%}  ({intent_correct}/{n})")
    print(f"  API JSON valid:       {metrics['api_json_valid_rate']:.1%}  ({api_json_valid}/{len(api_results)})")
    print(f"  API func_code match:  {metrics['api_func_code_match_rate']:.1%}  ({api_code_match}/{len(api_results)})")
    print(f"  API path match:       {metrics['api_path_match_rate']:.1%}  ({api_path_match}/{len(api_results)})")
    print(f"  API param accuracy:   {metrics['api_param_accuracy']:.1%}  ({param_total_correct}/{param_total})")
    print(f"  Doc format valid:     {metrics['doc_format_valid_rate']:.1%}  ({doc_format_valid}/{len(doc_results)})")
    print(f"  Doc answer match:     {metrics['doc_answer_match_rate']:.1%}  ({doc_answer_match}/{len(doc_results)})")
    print(f"  Avg time_response:    {metrics['avg_time_response']:.2f}s  (target <{config.TIME_RESPONSE_TARGET}s)")
    if missing_counter:
        print(f"\n  Top params MISSING (predict thiếu so với GT):")
        for k, v in missing_counter.most_common(10):
            print(f"    {k:<25} {v} lần")
    if extra_counter:
        print(f"\n  Top params EXTRA (predict thừa so với GT):")
        for k, v in extra_counter.most_common(10):
            print(f"    {k:<25} {v} lần")
    if wrong_counter:
        print(f"\n  Top params WRONG VALUE (giá trị sai):")
        for k, v in wrong_counter.most_common(10):
            print(f"    {k:<25} {v} lần")
    print(f"\n  Saved -> {out_pred}")
    print(f"  Saved -> {out_metrics}")
    print(f"  Saved -> {out_eval}")
    print(f"  Saved -> {out_api_diff}")

    if metrics["intent_accuracy"] < 0.95:
        print(f"\n  !! Intent accuracy < 95% — check INTENT_TOP_K={config.INTENT_TOP_K}")
    if metrics["avg_time_response"] > config.TIME_RESPONSE_TARGET:
        print(f"  !! avg time > {config.TIME_RESPONSE_TARGET}s — cần optimize")


if __name__ == "__main__":
    main()
