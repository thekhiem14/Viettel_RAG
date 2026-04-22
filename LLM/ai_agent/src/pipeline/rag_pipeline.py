from typing import Optional

from src.retrieval.vector_store import VectorStore
from src.retrieval.bm25_store import BM25Store
from src.retrieval.rrf import rrf_merge
from src.retrieval.reranker import Reranker
from src.llm.model import QwenModel
from src.utils.doc_extractor import extract_doc_id_from_row


PROMPT_TEMPLATE = """\
Dựa vào các đoạn tài liệu dưới đây, hãy chọn đáp án đúng cho câu hỏi.
Chỉ trả lời bằng chữ cái (A, B, C hoặc D). Nếu nhiều đáp án đúng, liệt kê liền nhau (ví dụ: AB).

--- TÀI LIỆU ---
{context}
--- HẾT TÀI LIỆU ---

Câu hỏi: {question}
A. {A}
B. {B}
C. {C}
D. {D}

Đáp án:"""


class RAGPipeline:
    def __init__(
        self,
        vector_store: VectorStore,
        bm25_store: BM25Store,
        reranker: Reranker,
        llm: QwenModel,
        top_k_retrieve: int = 20,
        top_k_rerank: int = 5,
    ):
        self.vector_store = vector_store
        self.bm25_store = bm25_store
        self.reranker = reranker
        self.llm = llm
        self.top_k_retrieve = top_k_retrieve
        self.top_k_rerank = top_k_rerank

    def run(
        self,
        question: str,
        options: dict,           # {'A': '...', 'B': '...', 'C': '...', 'D': '...'}
        note: Optional[str] = None,
    ) -> str:
        """
        Chạy toàn bộ RAG flow, trả về raw LLM answer string.
        """
        # 1. Extract doc filter
        doc_id = extract_doc_id_from_row(question, note)

        # 2. Hybrid retrieval
        vec_results = self.vector_store.search(question, k=self.top_k_retrieve, doc_id=doc_id)
        bm25_results = self.bm25_store.search(question, k=self.top_k_retrieve, doc_id=doc_id)

        merged = rrf_merge(vec_results, bm25_results, top_n=self.top_k_retrieve)

        # 3. Rerank
        top_chunks = self.reranker.rerank(question, merged, top_k=self.top_k_rerank)

        # 4. Build context
        context_parts = []
        for i, chunk in enumerate(top_chunks, 1):
            context_parts.append(f"[{i}] {chunk['full_text']}")
        context = "\n\n".join(context_parts)

        # 5. Build prompt và gọi LLM
        prompt = PROMPT_TEMPLATE.format(
            context=context,
            question=question,
            A=options.get('A', ''),
            B=options.get('B', ''),
            C=options.get('C', ''),
            D=options.get('D', ''),
        )

        return self.llm.generate(prompt, thinking=False)
