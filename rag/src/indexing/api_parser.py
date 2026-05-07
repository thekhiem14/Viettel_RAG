from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
from shared.types import APIEntry

_ALIAS_RE = re.compile(r"(\w+)\s*=\s*(\[[\s\S]*?\])\s*$", re.MULTILINE)


_KV_RE = re.compile(r'\{key:\s*(.*?),\s*value:\s*(.*?)\}')


def parse_alias_csv(csv_path: Path) -> dict[str, list[dict]]:
    """Parse Tài_liệu_config_API_Doc_alias_for_contest.csv → dict alias_name → list[{key, value}].

    File format: RFC 4180 double-quote wrapping, entries trải qua nhiều dòng.
    Sau khi unescape thành `name = [{key: X, value: Y}, ...]`, parse thủ công bằng regex.
    """
    raw = csv_path.read_text(encoding="utf-8-sig")
    # Unescape RFC 4180: "" → " rồi bỏ wrapper quotes
    text = raw.replace('""', '"').replace('"', '')
    aliases: dict[str, list[dict]] = {}
    for m in _ALIAS_RE.finditer(text):
        name = m.group(1)
        block = m.group(2)
        items = [
            {"key": kv.group(1).strip(), "value": kv.group(2).strip()}
            for kv in _KV_RE.finditer(block)
        ]
        if items:
            aliases[name] = items
    return aliases


def _parse_body(body) -> dict:
    if isinstance(body, dict):
        return body
    if isinstance(body, str):
        s = body.strip()
        if not s or s == "{}":
            return {}
        try:
            return json.loads(s)
        except json.JSONDecodeError:
            return {}
    return {}


def parse_api_csv(csv_path: Path) -> list[APIEntry]:
    """Parse Tài_liệu_config_API_Doc_api_for_contest.csv → list[APIEntry] (131 entries).

    Cột: func_code | name | description | Example question | Endpoint config (JSON blob)
    """
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    entries: list[APIEntry] = []

    for _, row in df.iterrows():
        ep = json.loads(row["Endpoint config"])

        request = ep.get("request", {})
        path = request.get("path", "")

        example_call = ep.get("example_call", [])
        example_body: dict = {}
        if isinstance(example_call, list) and example_call:
            example_body = _parse_body(example_call[0].get("body", {}))

        entries.append(APIEntry(
            func_code=str(row["func_code"]).strip(),
            name=str(row["name"]).strip(),
            description=str(row["description"]).strip(),
            example_question=str(row["Example question"]).strip(),
            path=path,
            required_params=ep.get("required_params", []) or [],
            optional_params=ep.get("optional_params", []) or [],
            response_schema=ep.get("response_schema", {}) or {},
            example_body=example_body,
        ))

    return entries
