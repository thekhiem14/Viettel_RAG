from __future__ import annotations

import json
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

import config


_aliases: dict[str, list[dict]] | None = None


def _load_aliases() -> dict[str, list[dict]]:
    global _aliases
    if _aliases is None:
        try:
            with open(config.API_ALIASES, encoding="utf-8") as f:
                _aliases = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            _aliases = {}
    return _aliases


def _norm(text: str) -> str:
    return unicodedata.normalize("NFC", text).strip().lower()


def _match_organization(question: str, entries: list[dict]) -> list[str]:
    """Exact match viết tắt (value) trong câu hỏi, VD: TTPMVT, TTPMQT.

    Chỉ match value (viết tắt toàn chữ hoa), không fuzzy key (tên đầy đủ)
    vì tên đầy đủ dễ match nhầm.
    """
    q = unicodedata.normalize("NFC", question)
    result: list[str] = []
    seen: set[str] = set()
    for e in entries:
        value = str(e.get("value", "")).strip()
        if not value or value in seen:
            continue
        # word-boundary check: value phải đứng riêng (space/dấu câu xung quanh)
        if value in q:
            idx = q.find(value)
            before = q[idx - 1] if idx > 0 else " "
            after = q[idx + len(value)] if idx + len(value) < len(q) else " "
            if not before.isalnum() and not after.isalnum():
                result.append(value)
                seen.add(value)
    return result


def _match_project_list(question: str, entries: list[dict]) -> list[int]:
    """project_info: tìm tên dự án 'BUxx.xxx' trong câu hỏi → trả list id."""
    q = unicodedata.normalize("NFC", question)
    result: list[int] = []
    seen: set[int] = set()
    for e in entries:
        name = str(e.get("projectName", "")).strip()
        pid = e.get("projectId")
        if name and pid is not None and name in q and int(pid) not in seen:
            result.append(int(pid))
            seen.add(int(pid))
    return result


def _match_customer(question: str, entries: list[dict]) -> list[str]:
    """customerList/customerDebt: match tên công ty dài (>= 6 chars) trong câu hỏi."""
    q_norm = _norm(question)
    result: list[str] = []
    seen: set[str] = set()
    for e in entries:
        key = str(e.get("key", "")).strip()
        value = str(e.get("value", "")).strip()
        if not key or not value or value in seen:
            continue
        if len(key) >= 6 and _norm(key) in q_norm:
            result.append(value)
            seen.add(value)
    return result


def match_aliases(question: str) -> dict[str, list]:
    """Trả về dict chỉ gồm 3 nhóm an toàn để rule-based extract:
      - organization: exact match viết tắt (TTPMVT, TTPMQT, ...)
      - projectList: tra bảng project_info tên → id
      - customerList / customerDebt: match tên công ty dài

    Tất cả enum List params khác (lcntType, projectType, projectStatus, ...)
    để LLM tự xử lý dựa vào description trong schema.
    """
    aliases = _load_aliases()
    out: dict[str, list] = {}

    for param, entries in aliases.items():
        if not isinstance(entries, list) or not entries:
            continue

        if param in ("organization", "orgAlias"):
            vals = _match_organization(question, entries)
            if vals:
                existing = out.get("organization", [])
                for v in vals:
                    if v not in existing:
                        existing.append(v)
                out["organization"] = existing

        elif param == "project_info":
            ids = _match_project_list(question, entries)
            if ids:
                out["projectList"] = ids

        elif param in ("customerList", "customerDebt"):
            vals = _match_customer(question, entries)
            if vals:
                out[param] = vals

        # Tất cả enum khác (projectType, projectStatus, lcntType, ...) bỏ qua
        # → để LLM đọc description và tự điền

    return out
