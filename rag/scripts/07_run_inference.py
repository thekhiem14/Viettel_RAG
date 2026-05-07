"""Run inference trên 617 test questions -> output JSON cho submission.

Usage:
    python rag/scripts/07_run_inference.py

Output:
    outputs/submission/result.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import config
from intent.src.md_parser import parse_test_md
from rag.src.pipeline.orchestrator import run_batch
from shared.utils.logger import get_logger

logger = get_logger("07_run_inference", config.LOGS_DIR)


def main() -> None:
    config.ensure_dirs()

    questions = parse_test_md(config.TEST_MD)
    if not questions:
        raise RuntimeError(f"No questions parsed from {config.TEST_MD}")

    print(f"[07_inference] running on {len(questions)} test questions...")
    t0 = time.perf_counter()

    results = run_batch(questions)

    total_time = time.perf_counter() - t0

    out_path = config.OUTPUTS_DIR / "submission" / "result.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(results, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"[07_inference] DONE — {len(results)} results in {total_time:.1f}s")
    print(f"  avg: {total_time / len(results):.2f}s/question")
    print(f"  saved -> {out_path}")


if __name__ == "__main__":
    main()
