import sys
sys.path.insert(0, "d:/Github-Project/Viettel_RAG")
import unittest.mock as mock
sys.modules["dotenv"] = mock.MagicMock()

from rag.src.chunking.heading_chunker import chunk_all_documents

all_c = chunk_all_documents()
doc_ids = set(c.doc_id for c in all_c)
sizes = [c.char_count for c in all_c]
print(f"Total: {len(all_c)} chunks | {len(doc_ids)} docs")
print(f"avg={sum(sizes)//len(sizes)} min={min(sizes)} max={max(sizes)}")
