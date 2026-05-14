"""Test api_pipeline_v2 trên 5 câu call_api đầu tiên trong Test_data.csv.

Usage:
    python rag/scripts/test_v2_5_questions.py

In kết quả ra terminal (không lưu file).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import config
from intent.src.md_parser import parse_test_csv
from rag.src.pipeline import api_pipeline_v2
from rag.src.pipeline.orchestrator import warmup
from shared.types import Question


N_QUESTIONS = 5


def _is_api_question(q: Question) -> bool:
    """call_api = không có note MCQ (A/B/C/D)."""
    return q.note is None or not q.note.strip()


def main() -> None:
    config.ensure_dirs()

    all_questions = parse_test_csv(config.TEST_CSV)
    api_questions = [q for q in all_questions if _is_api_question(q)]
    if not api_questions:
        raise RuntimeError("Không có câu call_api nào trong Test_data.csv")

    selected = api_questions[:N_QUESTIONS]
    print(f"[test_v2] Tìm thấy {len(api_questions)} câu call_api, chạy {len(selected)} câu đầu.\n")

    # Warmup (1 lần cho cả 5 câu)
    print("=" * 80)
    print("WARMUP")
    print("=" * 80)
    warmup()

    print("\n" + "=" * 80)
    print(f"RUN {len(selected)} QUESTIONS")
    print("=" * 80)

    results = []
    t_total = time.perf_counter()
    for i, q in enumerate(selected, 1):
        print(f"\n--- [{i}/{len(selected)}] id={q.id} ---")
        print(f"Q: {q.question}")
        result = api_pipeline_v2.run(q)
        print(f"function_result:\n{result['function_result']}")
        print(f"time_response: {result['time_response']:.2f}s")
        results.append(result)

    elapsed = time.perf_counter() - t_total

    # Summary cuối: in lại toàn bộ kết quả gọn
    print("\n" + "=" * 80)
    print("FINAL RESULTS")
    print("=" * 80)
    for r in results:
        print(f"\nid={r['id']}  func_code={r['function_code']}  time={r['time_response']:.2f}s")
        print(r["function_result"])

    print("\n" + "=" * 80)
    print(f"DONE — {len(results)} câu trong {elapsed:.1f}s (avg {elapsed/len(results):.2f}s/câu)")
    print("=" * 80)


if __name__ == "__main__":
    main()
