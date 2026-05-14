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
    """NFC + lowercase + strip accents for fuzzy contains."""
    return unicodedata.normalize("NFC", text).strip().lower()


def _norm_no_accent(text: str) -> str:
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text.lower().strip()


# Params nào dùng matching theo "value/key có xuất hiện trong question?"
# (alias_table key = tên param trong schema)
_ENUM_PARAMS = {
    "organization",
    "projectType",
    "projectStatus",
    "level",
    "position",
    "lcntOption",
    "lcntOptionDoing",
    "lcntType",
    "lcntDomainType",
    "bidPlanType",
    "dtmsType",
    "dtmsClass",
    "assetGroup",
    "procurementType",
    "isProbation",
    "priorityList",
    "hdStatus",
    "gtStatus",
    "trainGroup",
    "projectStatus",
    "orgAlias",
}

# Params đặc biệt: lookup theo tên → id/code
_LOOKUP_PARAMS = {
    "project_info": "projectList",   # alias key "project_info" → schema key "projectList"
    "customerList": "customerList",
    "customerDebt": "customerDebt",
}


def _match_enum(question: str, entries: list[dict]) -> list[str]:
    """Với mỗi entry {key, value}, nếu key/value xuất hiện trong question → thêm value."""
    q_norm = _norm(question)
    q_noacc = _norm_no_accent(question)
    matched: list[str] = []
    seen: set[str] = set()
    for e in entries:
        key = str(e.get("key", "")).strip()
        value = str(e.get("value", "")).strip()
        if not value:
            continue
        # Match: ưu tiên value (viết tắt) khớp chính xác, fallback key (tên đầy đủ)
        hit = False
        if value:
            v_norm = _norm(value)
            v_noacc = _norm_no_accent(value)
            if v_norm in q_norm or (len(v_noacc) >= 3 and v_noacc in q_noacc):
                hit = True
        if not hit and key:
            k_norm = _norm(key)
            k_noacc = _norm_no_accent(key)
            if k_norm in q_norm or (len(k_noacc) >= 4 and k_noacc in q_noacc):
                hit = True
        if hit and value not in seen:
            matched.append(value)
            seen.add(value)
    return matched


def _match_project_list(question: str, entries: list[dict]) -> list[int]:
    """project_info: tìm tên dự án 'BU01.xxx' trong question → trả list id."""
    q = unicodedata.normalize("NFC", question)
    result: list[int] = []
    seen: set[int] = set()
    for e in entries:
        name = str(e.get("projectName", "")).strip()
        pid = e.get("projectId")
        if name and pid is not None and name in q and pid not in seen:
            result.append(int(pid))
            seen.add(int(pid))
    return result


def _match_customer(question: str, entries: list[dict]) -> list[str]:
    q_norm = _norm(question)
    q_noacc = _norm_no_accent(question)
    result: list[str] = []
    seen: set[str] = set()
    for e in entries:
        key = str(e.get("key", "")).strip()
        value = str(e.get("value", "")).strip()
        if not key or not value:
            continue
        k_norm = _norm(key)
        k_noacc = _norm_no_accent(key)
        if k_norm in q_norm or (len(k_noacc) >= 6 and k_noacc in q_noacc):
            if value not in seen:
                result.append(value)
                seen.add(value)
    return result


def match_aliases(question: str) -> dict[str, list]:
    """Match câu hỏi với toàn bộ alias table, trả về dict {param_name: [values]}.

    Chỉ trả các key có ít nhất 1 match.
    """
    aliases = _load_aliases()
    out: dict[str, list] = {}

    for param, entries in aliases.items():
        if not isinstance(entries, list) or not entries:
            continue
        if param == "project_info":
            ids = _match_project_list(question, entries)
            if ids:
                out["projectList"] = ids
        elif param in {"customerList", "customerDebt"}:
            vals = _match_customer(question, entries)
            if vals:
                out[param] = vals
        elif param in _ENUM_PARAMS or param == "orgAlias":
            vals = _match_enum(question, entries)
            if vals:
                # orgAlias dùng chung cột với organization
                target = "organization" if param == "orgAlias" else param
                existing = out.get(target, [])
                for v in vals:
                    if v not in existing:
                        existing.append(v)
                out[target] = existing
    return out
