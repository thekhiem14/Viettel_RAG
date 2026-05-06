from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from shared.types import Question

_TABLE_ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|(.+?)\|(.+?)\|", re.MULTILINE)


def _clean_cell(s: str) -> str:
    return s.strip().replace("\\n", "\n")


def parse_example_md(md_path: Path) -> list[Question]:
    """Parse Example_Data_RAG.md → list[Question].

    Dùng để train/eval classifier. note='nan' → call_api, else → call_document.
    """
    text = md_path.read_text(encoding="utf-8")
    questions: list[Question] = []

    for m in _TABLE_ROW_RE.finditer(text):
        try:
            qid = int(m.group(1).strip())
        except ValueError:
            continue
        question = _clean_cell(m.group(2))
        note_raw = _clean_cell(m.group(3))
        note = None if note_raw.lower() in {"nan", "", "none"} else note_raw
        if question:
            questions.append(Question(id=qid, question=question, note=note))

    return questions


def parse_test_md(md_path: Path) -> list[Question]:
    """Parse Test_Data_RAG.md → list[Question] (617 câu, không có ground truth)."""
    return parse_example_md(md_path)
