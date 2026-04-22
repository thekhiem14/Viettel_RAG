from typing import Optional
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


class VectorStore:
    def __init__(self, faiss_dir: str, embedding_model: str = "BAAI/bge-m3"):
        self.embeddings = HuggingFaceEmbeddings(
            model_name=embedding_model,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )
        self.vs = FAISS.load_local(
            faiss_dir,
            self.embeddings,
            allow_dangerous_deserialization=True,
        )
        print(f"VectorStore loaded từ {faiss_dir}")

    def search(self, query: str, k: int = 20, doc_id: Optional[str] = None) -> list[dict]:
        """
        Trả về list of {chunk_id, doc_id, heading_path, full_text, score}.
        Nếu doc_id được cung cấp, chỉ trả kết quả thuộc doc đó.
        """
        fetch_k = k * 4 if doc_id else k * 2
        results = self.vs.similarity_search_with_score(query, k=fetch_k)

        output = []
        for doc, dist_score in results:
            meta = doc.metadata
            if doc_id and meta.get('doc_id') != doc_id:
                continue
            output.append({
                'chunk_id': meta.get('chunk_id', ''),
                'doc_id': meta.get('doc_id', ''),
                'heading_path': meta.get('heading_path', ''),
                'full_text': doc.page_content,
                'vector_score': float(1 - dist_score),  # convert L2 distance → similarity
            })
            if len(output) >= k:
                break

        return output
