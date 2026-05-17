"""Chạy toàn bộ Test_data.csv và xuất file submission đúng format nộp bài.

Usage:
    python rag/scripts/make_submission.py
    python rag/scripts/make_submission.py --no-warmup   # nếu model đã load sẵn

Output:
    outputs/submission/submission.csv
"""
from __future__ import annotations

import csv
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import config
from intent.src.md_parser import parse_test_csv
from rag.src.pipeline.orchestrator import run_batch, warmup


def _format_doc(answer: str) -> str:
    """Chuyển "AB" → {"numbers": 2, "result": "A,B"}"""
    letters = [c for c in answer.upper() if c in "ABCD"]
    return json.dumps(
        {"numbers": len(letters), "result": ",".join(letters)},
        ensure_ascii=False,
    )


def _format_api(raw: str, path: str = "") -> str:
    """Wrap body JSON + path thành func_param."""
    try:
        body = json.loads(raw)
        return json.dumps({"path": path, "body": body}, ensure_ascii=False)
    except (json.JSONDecodeError, AttributeError):
        return raw


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-warmup", action="store_true")
    args = parser.parse_args()

    config.ensure_dirs()

    questions = parse_test_csv(config.TEST_CSV)
    print(f"[submission] {len(questions)} câu hỏi")

    if not args.no_warmup:
        warmup()

    t0 = time.perf_counter()
    results = run_batch(questions)
    elapsed = time.perf_counter() - t0

    out_path = config.OUTPUTS_DIR / "submission" / "submission.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["id", "func_code", "func_param", "time"])
        for r in results:
            func_code = r["function_code"]
            raw = r["function_result"]
            if func_code == "call_document":
                func_param = _format_doc(raw)
            else:
                func_param = _format_api(raw, path=r.get("api_path", ""))
            writer.writerow([r["id"], func_code, func_param, r["time_response"]])
            rows.append((r["id"], func_code, raw, func_param, r["time_response"]))

    eval_path = config.OUTPUTS_DIR / "submission" / "submission_eval.csv"
    with open(eval_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["id", "func_code", "raw_result", "func_param", "time"])
        for id_, fc, raw, fp, t in rows:
            writer.writerow([id_, fc, raw, fp, t])

    print(f"\n[submission] DONE — {len(results)} câu trong {elapsed:.1f}s")
    print(f"  avg: {elapsed / len(results):.2f}s/câu")
    print(f"  saved -> {out_path}")


if __name__ == "__main__":
    main()
