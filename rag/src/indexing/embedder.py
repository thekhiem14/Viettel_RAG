from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
import config
from shared.types import APIEntry, Chunk

_model = None  # lazy singleton


def _get_model():
    global _model
    if _model is None:
        from FlagEmbedding import FlagModel
        _model = FlagModel(
            config.EMBED_MODEL,
            use_fp16=True,
            query_instruction_for_retrieval="Represent this sentence for searching relevant passages: ",
        )
    return _model


class Embedder:
    """Wrapper bge-m3: encode texts → L2-normalized vectors (N, 1024)."""

    def encode(self, texts: list[str], batch_size: int = 32) -> np.ndarray:
        """Encode list of texts, trả về float32 array shape (N, 1024), L2-normalized."""
        model = _get_model()
        embeddings = model.encode(texts, batch_size=batch_size)
        norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
        norms = np.where(norms == 0, 1.0, norms)
        return (embeddings / norms).astype(np.float32)

    def encode_query(self, text: str) -> np.ndarray:
        """Encode single query, shape (1024,), L2-normalized."""
        return self.encode([text])[0]

    def encode_chunks(self, chunks: list[Chunk], batch_size: int = 32) -> np.ndarray:
        """Encode document chunks — dùng chunk.text (đã có breadcrumb prefix).

        Returns: float32 array shape (N, 1024), L2-normalized.
        """
        texts = [c.text for c in chunks]
        return self.encode(texts, batch_size=batch_size)

    def encode_api_entries(self, entries: list[APIEntry], batch_size: int = 32) -> np.ndarray:
        """Encode API entries — concat name + description + example_question.

        Ba field này bổ sung nhau: name (ngắn, chính xác), description (ngữ nghĩa),
        example_question (gần với cách user đặt câu hỏi thực tế).

        Returns: float32 array shape (N, 1024), L2-normalized.
        """
        texts = [f"{e.name} {e.description} {e.example_question}" for e in entries]
        return self.encode(texts, batch_size=batch_size)
