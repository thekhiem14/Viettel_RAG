"""
Script one-time: chunk toàn bộ main.md files → data/chunks/chunks.json
Chạy: python scripts/build_chunks.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.chunking.chunker import chunk_all_documents

TRAINING_OUTPUT_DIR = Path(__file__).parent.parent.parent / "training_data_update" / "output"
CHUNKS_OUTPUT = Path(__file__).parent.parent / "data" / "chunks" / "chunks.json"

if __name__ == "__main__":
    CHUNKS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    total = chunk_all_documents(str(TRAINING_OUTPUT_DIR), str(CHUNKS_OUTPUT))
    print(f"\nHoàn thành: {total} chunks")
