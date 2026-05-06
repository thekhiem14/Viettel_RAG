"""Eval pipeline trên 100 example questions (50 call_doc + 50 call_api).

Metrics:
  - Intent accuracy
  - call_api: JSON validity, func_code match (nếu có ground truth)
  - call_document: answer format valid (A/B/C/D)
  - Avg time_response

Usage:
    python rag/scripts/06_eval.py

Output:
    outputs/eval/predictions.jsonl
    outputs/eval/metrics.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import config
from intent.src.md_parser import parse_example_md
from rag.src.pipeline.orchestrator import run_batch
from shared.utils.io import save_json, save_jsonl
from shared.utils.logger import get_logger

logger = get_logger("06_eval", config.LOGS_DIR)


def main() -> None:
    config.ensure_dirs()

    questions = parse_example_md(config.EXAMPLE_MD)
    if not questions:
        raise RuntimeError(f"No questions parsed from {config.EXAMPLE_MD}")

    print(f"[06_eval] running on {len(questions)} questions...")
    t0 = time.perf_counter()

    results = run_batch(questions)

    total_time = time.perf_counter() - t0
    avg_time = total_time / len(results)

    # Save predictions
    out_pred = config.OUTPUTS_DIR / "eval" / "predictions.jsonl"
    save_jsonl(out_pred, results)

    # Compute metrics
    api_results = [r for r in results if r["function_code"] == "call_api"]
    doc_results = [r for r in results if r["function_code"] == "call_document"]

    api_json_valid = 0
    for r in api_results:
        try:
            parsed = json.loads(r["function_result"])
            if "func_code" in parsed and "path" in parsed and "body" in parsed:
                api_json_valid += 1
        except Exception:
            pass

    doc_format_valid = 0
    import re
    ans_re = re.compile(r"^[A-D]{1,4}$")
    for r in doc_results:
        if ans_re.match(r["function_result"].strip()):
            doc_format_valid += 1

    time_responses = [r["time_response"] for r in results]
    metrics = {
        "total": len(results),
        "api_count": len(api_results),
        "doc_count": len(doc_results),
        "api_json_valid_rate": api_json_valid / len(api_results) if api_results else 0,
        "doc_format_valid_rate": doc_format_valid / len(doc_results) if doc_results else 0,
        "avg_time_response": sum(time_responses) / len(time_responses),
        "total_wall_time": round(total_time, 2),
    }

    out_metrics = config.OUTPUTS_DIR / "eval" / "metrics.json"
    save_json(out_metrics, metrics)

    print(f"[06_eval] DONE")
    print(f"  API JSON valid: {metrics['api_json_valid_rate']:.1%} ({api_json_valid}/{len(api_results)})")
    print(f"  Doc format valid: {metrics['doc_format_valid_rate']:.1%} ({doc_format_valid}/{len(doc_results)})")
    print(f"  Avg time: {metrics['avg_time_response']:.2f}s  (target: <{config.TIME_RESPONSE_TARGET}s)")
    print(f"  Saved → {out_pred}")
    print(f"  Saved → {out_metrics}")

    if metrics["avg_time_response"] > config.TIME_RESPONSE_TARGET:
        print(f"  ⚠ avg time > {config.TIME_RESPONSE_TARGET}s — cần optimize")


if __name__ == "__main__":
    main()
