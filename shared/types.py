from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Question:
    id: int
    question: str
    note: str | None = None  # "A, ...\n B, ...\n C, ...\n D, ..." — chỉ có trong call_document


@dataclass
class Chunk:
    chunk_id: str       # "Public_001_012"
    doc_id: str         # "Public_001"
    heading_path: str   # "Dịch vụ > Nhà thông minh > Cảm biến"
    level: int
    char_count: int
    text: str           # có prefix breadcrumb: "[Public_001 > ...]\nNội dung..."


@dataclass
class APIEntry:
    func_code: str
    name: str
    description: str
    example_question: str
    path: str
    required_params: list[dict] = field(default_factory=list)
    optional_params: list[dict] = field(default_factory=list)
    response_schema: dict = field(default_factory=dict)
    example_body: dict = field(default_factory=dict)


@dataclass
class RetrievalHit:
    id: str       # chunk_id hoặc func_code
    score: float
    source: str   # "bm25" | "faiss" | "fuzzy"
    rank: int
