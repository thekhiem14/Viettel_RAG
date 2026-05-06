"""Build API indices: parse Excel → 131 APIEntry → encode → save FAISS + BM25 + Fuzzy + schemas.

Usage:
    python rag/scripts/03_build_api_index.py            # skip nếu artifact đã tồn tại
    python rag/scripts/03_build_api_index.py --force    # rebuild

Prerequisites:
    - Excel file: data/Tài liệu config API.xlsx, Sheet `Doc_api_for_contest` (131 rows)
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import config
from rag.src.indexing.api_parser import parse_api_excel
from rag.src.indexing.bm25_store import BM25Store
from rag.src.indexing.embedder import Embedder
from rag.src.indexing.faiss_store import FaissStore
from rag.src.indexing.fuzzy_store import FuzzyStore
from shared.utils.io import save_json
from shared.utils.timer import timed

API_XLSX = config.DATA_DIR / "Tài liệu config API.xlsx"


def main(force: bool = False) -> None:
    config.ensure_dirs()

    artifacts = [config.API_SCHEMAS, config.API_FAISS, config.API_BM25, config.API_FUZZY]
    if not force and all(p.exists() for p in artifacts):
        print(f"[03_build_api] all artifacts exist → skip. Use --force to rebuild.")
        for p in artifacts:
            print(f"  - {p}")
        return

    if not API_XLSX.exists():
        raise FileNotFoundError(f"API Excel not found: {API_XLSX}")

    with timed("parse API Excel"):
        entries = parse_api_excel(API_XLSX)
    print(f"[03_build_api] parsed {len(entries)} API entries from {API_XLSX.name}")

    with timed("save schemas.json"):
        schemas = {e.func_code: asdict(e) for e in entries}
        save_json(config.API_SCHEMAS, schemas)
    print(f"[03_build_api] saved schemas → {config.API_SCHEMAS}")

    ids = [e.func_code for e in entries]
    bm25_texts = [f"{e.name} {e.description} {e.example_question}" for e in entries]
    fuzzy_targets = [
        {"id": e.func_code, "func_code": e.func_code, "name": e.name, "text": f"{e.name} {e.description}"}
        for e in entries
    ]

    with timed("embed API entries (bge-m3)"):
        embedder = Embedder()
        embeddings = embedder.encode_api_entries(entries)
    print(f"[03_build_api] embeddings shape: {embeddings.shape}")

    with timed("build + save FAISS"):
        faiss_store = FaissStore()
        faiss_store.build(embeddings, ids)
        faiss_store.save(config.API_FAISS)
    print(f"[03_build_api] saved FAISS → {config.API_FAISS}")

    with timed("build + save BM25 (pyvi segment)"):
        bm25_store = BM25Store()
        bm25_store.build(bm25_texts, ids)
        bm25_store.save(config.API_BM25)
    print(f"[03_build_api] saved BM25 → {config.API_BM25}")

    with timed("build + save Fuzzy"):
        fuzzy_store = FuzzyStore()
        fuzzy_store.build(fuzzy_targets)
        fuzzy_store.save(config.API_FUZZY)
    print(f"[03_build_api] saved Fuzzy → {config.API_FUZZY}")

    print(f"[03_build_api] DONE. {len(entries)} API entries indexed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="Rebuild even if artifacts exist")
    args = parser.parse_args()
    main(force=args.force)
