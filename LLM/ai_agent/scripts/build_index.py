"""
Script one-time: đọc chunks.json → build FAISS + BM25 → lưu data/index/
Chạy: python scripts/build_index.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.indexing.indexer import Indexer

CHUNKS_PATH = Path(__file__).parent.parent / "data" / "chunks" / "chunks.json"
INDEX_DIR   = Path(__file__).parent.parent / "data" / "index"

if __name__ == "__main__":
    if not CHUNKS_PATH.exists():
        print(f"Không tìm thấy {CHUNKS_PATH}. Chạy build_chunks.py trước!")
        sys.exit(1)

    indexer = Indexer(index_dir=str(INDEX_DIR))
    indexer.build(chunks_path=str(CHUNKS_PATH))
