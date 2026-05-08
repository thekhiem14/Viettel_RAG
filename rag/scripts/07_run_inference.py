"""Run inference trên test questions -> output CSV cho submission.

Usage:
    python rag/scripts/07_run_inference.py

Output:
    outputs/submission/result.csv

Format theo đề bài: utf-8 CSV, cột id,func_code,func_param,time
"""
from __future__ import annotations

import csv
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import config
from intent.src.md_parser import parse_test_md
from rag.src.pipeline.orchestrator import run_batch, warmup
from shared.utils.logger import get_logger

logger = get_logger("07_run_inference", config.LOGS_DIR)


def main() -> None:
    config.ensure_dirs()

    # Warm-up TRƯỚC khi đọc file test để time_response không bị tính cold-start
    print("[07_inference] warming up models...")
    t_warm = time.perf_counter()
    warmup()
    print(f"[07_inference] warm-up done in {time.perf_counter() - t_warm:.1f}s\n")

    questions = parse_test_md(config.TEST_MD)
    if not questions:
        raise RuntimeError(f"No questions parsed from {config.TEST_MD}")

    print(f"[07_inference] running on {len(questions)} test questions...")
    t0 = time.perf_counter()

    results = run_batch(questions)

    total_time = time.perf_counter() - t0

    out_path = config.OUTPUTS_DIR / "submission" / "result.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "func_code", "func_param", "time"])
        for r in results:
            writer.writerow([
                r["id"],
                r["function_code"],
                r["function_result"],
                r["time_response"],
            ])

    print(f"[07_inference] DONE — {len(results)} results in {total_time:.1f}s")
    print(f"  avg: {total_time / len(results):.2f}s/question")
    print(f"  saved -> {out_path}")


if __name__ == "__main__":
    main()
