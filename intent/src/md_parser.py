from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from shared.types import Question


def parse_example_csv(csv_path: Path) -> list[Question]:
    """Parse example_data_example_question.csv → list[Question].

    Cột: id | fun_question | note
    note rỗng → call_api, có giá trị → call_document (chứa options A/B/C/D).
    """
    questions: list[Question] = []
    with open(csv_path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            try:
                qid = int(row["id"])
            except (ValueError, KeyError):
                continue
            question = row.get("fun_question", "").strip()
            note_raw = row.get("note", "").strip()
            note = None if note_raw.lower() in {"nan", "", "none"} else note_raw
            if question:
                questions.append(Question(id=qid, question=question, note=note))
    return questions


def parse_test_csv(csv_path: Path) -> list[Question]:
    """Parse Test_data.csv → list[Question] (617 câu, không có ground truth)."""
    return parse_example_csv(csv_path)


# --- Backward-compat aliases ---
def parse_example_md(csv_path: Path) -> list[Question]:
    return parse_example_csv(csv_path)


def parse_test_md(csv_path: Path) -> list[Question]:
    return parse_test_csv(csv_path)
