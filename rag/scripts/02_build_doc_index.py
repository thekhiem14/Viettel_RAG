"""Build document indices: chunk markdown → encode → save FAISS + BM25 + chunks.jsonl.

Usage:
    python rag/scripts/02_build_doc_index.py            # skip nếu artifact đã tồn tại
    python rag/scripts/02_build_doc_index.py --force    # rebuild

Prerequisites:
    - Markdown files đã convert sẵn ở config.MINERU_OUT_DIR (mỗi doc 1 thư mục Public_XXX/main.md)
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import config
from rag.src.chunking.heading_chunker import chunk_all_documents
from rag.src.indexing.bm25_store import BM25Store
from rag.src.indexing.embedder import Embedder
from rag.src.indexing.faiss_store import FaissStore
from shared.utils.io import save_jsonl
from shared.utils.timer import timed


def main(force: bool = False) -> None:
    config.ensure_dirs()

    artifacts = [config.DOC_CHUNKS, config.DOC_FAISS, config.DOC_BM25]
    if not force and all(p.exists() for p in artifacts):
        print(f"[02_build_doc] all artifacts exist → skip. Use --force to rebuild.")
        for p in artifacts:
            print(f"  - {p}")
        return

    with timed("chunk_all_documents"):
        chunks = chunk_all_documents()
    print(f"[02_build_doc] chunked {len(chunks)} chunks from {config.MINERU_OUT_DIR}")
    if not chunks:
        raise RuntimeError(f"No chunks produced. Check MINERU_OUT_DIR={config.MINERU_OUT_DIR}")

    with timed("save chunks.jsonl"):
        save_jsonl(config.DOC_CHUNKS, (asdict(c) for c in chunks))
    print(f"[02_build_doc] saved chunks → {config.DOC_CHUNKS}")

    ids = [c.chunk_id for c in chunks]
    texts = [c.text for c in chunks]

    with timed("embed chunks (bge-m3)"):
        embedder = Embedder()
        embeddings = embedder.encode_chunks(chunks)
    print(f"[02_build_doc] embeddings shape: {embeddings.shape}")

    with timed("build + save FAISS"):
        faiss_store = FaissStore()
        faiss_store.build(embeddings, ids)
        faiss_store.save(config.DOC_FAISS)
    print(f"[02_build_doc] saved FAISS → {config.DOC_FAISS}")

    with timed("build + save BM25 (pyvi segment)"):
        bm25_store = BM25Store()
        bm25_store.build(texts, ids)
        bm25_store.save(config.DOC_BM25)
    print(f"[02_build_doc] saved BM25 → {config.DOC_BM25}")

    print(f"[02_build_doc] DONE. {len(chunks)} chunks indexed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="Rebuild even if artifacts exist")
    args = parser.parse_args()
    main(force=args.force)
