"""Chạy doc pipeline từ câu hỏi thứ 51 trong Test_data.csv.

Usage:
    python rag/scripts/run_from_51.py
    python rag/scripts/run_from_51.py --start 51 --end 60
"""
from __future__ import annotations

import argparse
import csv
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import config
from intent.src.md_parser import parse_test_csv
from rag.src.pipeline.orchestrator import run_batch, warmup


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=51, help="Câu bắt đầu (1-indexed, default=51)")
    parser.add_argument("--end",   type=int, default=None, help="Câu kết thúc inclusive (default=hết file)")
    parser.add_argument("--no-warmup", action="store_true", help="Bỏ qua warmup")
    args = parser.parse_args()

    config.ensure_dirs()

    questions = parse_test_csv(config.TEST_CSV)
    total = len(questions)
    print(f"[run_from_51] Tổng số câu trong file: {total}")

    start_idx = args.start - 1
    end_idx   = args.end if args.end is None else args.end
    subset = questions[start_idx:end_idx]
    print(f"[run_from_51] Chạy câu {args.start} → {args.end or total}  ({len(subset)} câu)")

    if not args.no_warmup:
        warmup()

    t0 = time.perf_counter()
    results = run_batch(subset)
    elapsed = time.perf_counter() - t0

    out_path = config.OUTPUTS_DIR / "submission" / f"result_from_{args.start}.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "func_code", "func_param", "time"])
        for r in results:
            writer.writerow([r["id"], r["function_code"], r["function_result"], r["time_response"]])

    print(f"\n[run_from_51] DONE — {len(results)} câu trong {elapsed:.1f}s")
    print(f"  avg: {elapsed / len(results):.2f}s/câu")
    print(f"  saved -> {out_path}")


if __name__ == "__main__":
    main()
