from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
from shared.types import APIEntry


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


def parse_api_excel(xlsx_path: Path, sheet: str = "Doc_api_for_contest") -> list[APIEntry]:
    """Parse `Tài liệu config API.xlsx` → list[APIEntry] (131 entries).

    Sheet `Doc_api_for_contest` có 5 cột:
      func_code | name | description | Example question | Endpoint config (JSON blob)

    Endpoint config blob chứa: request, example_call, required_params, optional_params,
    response_schema, structured_output (skip), allow_empty_result (skip).
    """
    df = pd.read_excel(xlsx_path, sheet_name=sheet)
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
