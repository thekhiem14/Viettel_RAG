import json
import pickle
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from rank_bm25 import BM25Okapi


EMBEDDING_MODEL = "BAAI/bge-m3"


class Indexer:
    def __init__(self, index_dir: str, embedding_model: str = EMBEDDING_MODEL):
        self.index_dir = Path(index_dir)
        self.faiss_dir = self.index_dir / "faiss"
        self.bm25_path = self.index_dir / "bm25.pkl"
        self.metadata_path = self.index_dir / "metadata.json"

        print(f"Đang load embedding model: {embedding_model}")
        self.embeddings = HuggingFaceEmbeddings(
            model_name=embedding_model,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )

    def build(self, chunks_path: str):
        """
        Đọc chunks.json → build FAISS + BM25 → lưu ra index_dir.
        """
        with open(chunks_path, encoding='utf-8') as f:
            chunks = json.load(f)

        print(f"Đang build index từ {len(chunks)} chunks...")
        self.index_dir.mkdir(parents=True, exist_ok=True)
        self.faiss_dir.mkdir(parents=True, exist_ok=True)

        # Build FAISS
        docs = [
            Document(
                page_content=c['full_text'],
                metadata={
                    'doc_id': c['doc_id'],
                    'heading_path': c['heading_path'],
                    'level': c['level'],
                    'chunk_id': c['chunk_id'],
                    'char_count': c['char_count'],
                },
            )
            for c in chunks
        ]

        print("  Đang embed và build FAISS...")
        vector_store = FAISS.from_documents(docs, self.embeddings)
        vector_store.save_local(str(self.faiss_dir))
        print(f"  FAISS lưu tại {self.faiss_dir}")

        # Build BM25 (tokenize bằng whitespace, phù hợp tiếng Việt)
        raw_texts = [c['full_text'] for c in chunks]
        tokenized = [text.split() for text in raw_texts]
        bm25 = BM25Okapi(tokenized)

        bm25_payload = {
            'bm25': bm25,
            'raw_texts': raw_texts,
            'metadata': [
                {
                    'doc_id': c['doc_id'],
                    'heading_path': c['heading_path'],
                    'chunk_id': c['chunk_id'],
                }
                for c in chunks
            ],
        }
        with open(self.bm25_path, 'wb') as f:
            pickle.dump(bm25_payload, f)
        print(f"  BM25 lưu tại {self.bm25_path}")

        # Lưu metadata riêng để tiện tra cứu
        with open(self.metadata_path, 'w', encoding='utf-8') as f:
            json.dump([c for c in chunks], f, ensure_ascii=False, indent=2)
        print(f"  Metadata lưu tại {self.metadata_path}")

        print(f"\nHoàn thành build index: {len(chunks)} chunks")

    def load_faiss(self) -> FAISS:
        vs = FAISS.load_local(
            str(self.faiss_dir),
            self.embeddings,
            allow_dangerous_deserialization=True,
        )
        return vs

    def load_bm25(self) -> dict:
        with open(self.bm25_path, 'rb') as f:
            return pickle.load(f)
