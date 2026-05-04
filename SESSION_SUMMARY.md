# Session Summary — Viettel RAG Project

## Tổng quan dự án

**Mục tiêu**: RAG chatbot xử lý 2 task:
- `call_document`: Trích xuất đáp án MCQ từ 398 PDF (Public_001 → Public_398)
- `call_api`: Chọn 1 trong 131 API và điền params

**Input**: `{id, fun_question, note}`
- `note` = null → call_api (50 câu)
- `note` = "A, ...\n B, ...\n C, ...\n D, ..." → call_document (50 câu)

**Output**: `{id, function_code, function_result, time_response}`

---

## Data structure

### Chunk (call_document)
```python
@dataclass
class Chunk:
    chunk_id: str          # "Public_001_012"
    doc_id: str            # "Public_001"
    heading_path: str      # "Dịch vụ > Nhà thông minh"
    level: int
    char_count: int
    text: str              # "[Public_001 > ...]\nNội dung..."
```

### APIEntry (call_api)
```python
@dataclass
class APIEntry:
    func_code: str         # "get_defect_rate_monthly"
    name: str              # "Lấy defect rate theo tháng" (tiếng Việt)
    description: str
    example_question: str
    path: str
    required_params: list[dict]
    optional_params: list[dict]
    response_schema: dict
    example_body: dict
```

### RetrievalHit (chung cho cả 2)
```python
@dataclass
class RetrievalHit:
    id: str                # chunk_id hoặc func_code
    score: float           # [0, 1]
    source: str            # "bm25" | "faiss" | "fuzzy"
    rank: int
```

---

## File structure hiện tại

```
Viettel_RAG/
├── config.py                           # ✓ XONG — 1 file cấu hình chung
├── PLAN.md                             # ✓ CẬP NHẬT — thiết kế chi tiết
├── ARCHITECTURE.md                     # ✓ CẬP NHẬT — cấu trúc folder
├── shared/
│   ├── types.py                        # ✓ XONG — Chunk, APIEntry, RetrievalHit
│   └── utils/
│       ├── logger.py                   # ✓ XONG
│       ├── timer.py                    # ✓ XONG
│       ├── vi_text.py                  # ✓ XONG — segment() cache
│       └── io.py                       # ✓ XONG — load/save atomic
├── rag/
│   └── src/
│       ├── chunking/
│       │   └── heading_chunker.py       # ✓ XONG — chỉ cho document
│       └── indexing/
│           ├── embedder.py             # ✓ XONG — encode_chunks() + encode_api_entries()
│           ├── faiss_store.py          # ✓ XONG — không thay đổi, generic
│           ├── bm25_store.py           # ✓ XONG — không thay đổi, generic
│           └── fuzzy_store.py          # ✓ SỬA — fuzzy trên name+description (tiếng Việt)
├── intent/                             # ⏳ PLACEHOLDER
├── data/                               # ⏳ INPUT
└── artifacts/                          # ⏳ OUTPUT (build scripts sẽ tạo)
```

---

## Công việc đã hoàn thành

### 1. Cấu hình (config.py)
- ✓ Single source of truth cho paths, models, hyperparams
- ✓ `ensure_dirs()` helper
- ✓ Hỗ trợ override via env vars (cho Colab)
- ✓ Bug fix: `os.getenv()` wrapper cho Path defaults

### 2. Data types (shared/types.py)
- ✓ `Chunk` — chunk_id, doc_id, heading_path, level, char_count, text
- ✓ `APIEntry` — func_code, name, description, example_question, path, params, schema, body
- ✓ `RetrievalHit` — id, score, source, rank (chung cho cả 2 pipeline)
- ✓ `Question` — id, question, note

### 3. Utility files
- ✓ `logger.py` — JSON formatter, stdout + file handlers
- ✓ `timer.py` — context manager + `timed()` wrapper
- ✓ `vi_text.py` — `segment()` with `@lru_cache(10_000)`
- ✓ `io.py` — atomic write (tmp → rename)

### 4. Chunking (heading_chunker.py)
- ✓ `chunk_document(md_path, doc_id)` — parse 1 file
- ✓ `chunk_all_documents()` — batch process
- ✓ Heading-based + breadcrumb prefix
- ✓ Rules: <80 skip, 80-600 = 1 chunk, >600 split + overlap 80

### 5. Embedder (embedder.py)
- ✓ Lazy singleton model loading
- ✓ `encode(texts) → (N, 1024)` L2-normalized
- ✓ `encode_query(text) → (1024,)`
- ✓ **NEW**: `encode_chunks(chunks)` — dùng chunk.text
- ✓ **NEW**: `encode_api_entries(entries)` — concat name+description+example_question

### 6. Stores (faiss_store, bm25_store, fuzzy_store)
- ✓ **FaissStore**: IndexFlatIP, filter_fn cho doc-level filtering
- ✓ **BM25Store**: BM25Okapi + pyvi segment, corpus persist
- ✓ **FuzzyStore**: RapidFuzz WRatio
  - **BUG FIX**: import `fuzz` thay vì `rf_utils.default_process`
  - **DESIGN FIX**: target text = `name + description` (tiếng Việt), KHÔNG phải func_code

### 7. PLAN.md & ARCHITECTURE.md
- ✓ Cập nhật với 131 APIs (không phải 136)
- ✓ Data analysis từ Excel thực tế
- ✓ Fuzzy logic giải thích chi tiết
- ✓ 5 retrieval strategies documented

---

## Công việc vướng mắc / cần xem xét

### 1. Build scripts (chưa viết)
**Cấu trúc planned:**
```
scripts/
├── 01_chunk_docs.py          # chunk_all_documents() → DOC_CHUNKS
├── 02_build_doc_index.py     # load chunks → embed_chunks → faiss/bm25
└── 03_build_api_index.py     # parse API Excel → embed_api → faiss/bm25/fuzzy
```

**Lưu ý kỹ**:
- `02_build_doc_index.py`: concat field = `chunk.text` (đã có breadcrumb)
- `03_build_api_index.py`: concat field = `f"{e.name} {e.description} {e.example_question}"`
- Fuzzy target = `{"id": func_code, "text": f"{name} {description}"}`

### 2. RRF fusion (rrf.py — chưa viết)
**Input**: 3 danh sách `list[RetrievalHit]` từ FAISS, BM25, Fuzzy (hoặc không)
**Logic**: Reciprocal Rank Fusion — `score(d) = Σ 1/(K + rank_i(d))`
**Output**: top-5 merged

**5 retrieval strategies để eval:**
1. FAISS only
2. BM25 only
3. Fuzzy only (call_api)
4. RRF hybrid (cả 3)
5. Dynamic-k (FAISS top-3 + 1 unique BM25 + 1 unique Fuzzy)

### 3. Retriever layers (chưa viết)
```
rag/src/retrieval/
├── doc_retriever.py    # doc-level filter + hybrid search + rerank
├── api_retriever.py    # RRF top-5 từ 3 nguồn (không rerank)
├── reranker.py         # cross-encoder bge-reranker-v2-m3
└── rrf.py              # merge logic
```

### 4. Pipelines (chưa viết)
```
rag/src/pipeline/
├── doc_pipeline.py     # chunk → embed → retrieve → rerank → LLM → answer
├── api_pipeline.py     # query → retrieve top-5 → LLM → JSON
└── orchestrator.py     # classifier → route → pipeline
```

### 5. Intent classifier (chưa viết)
```
intent/
├── classifier.py       # TF-IDF + Logistic Regression
└── features.py         # regex detect A/B/C/D pattern
```

### 6. LLM module (chưa viết)
```
rag/src/llm/
├── qwen.py            # wrapper Qwen3-4B (4-bit)
├── prompts.py         # template prompts (call_document CoT, call_api JSON)
└── json_validator.py  # 3-tier JSON validation
```

---

## Design decisions & architecture

### Embedder strategy
- **1 model**: bge-m3 cho cả doc + api
- **2 methods**: `encode_chunks()` + `encode_api_entries()` — explicit about field concatenation
- **Separate indices**: `DOC_FAISS` vs `API_FAISS` (different embeddings, different IDs)

### Store strategy
- **Generic stores**: FaissStore, BM25Store, FuzzyStore không biết doc vs api
- **Separation of concerns**: Logic "field nào" nằm ở build scripts, không ở stores
- **FuzzyStore**: chỉ cho call_api (API names + descriptions tiếng Việt)
- **FaissStore.filter_fn**: enable doc-level filtering hiệu quả

### Retrieval strategy
- **call_document**: FAISS (with filter_fn) + BM25 (post-filter) → RRF → Rerank → top-5 → LLM
- **call_api**: FAISS + BM25 + Fuzzy → RRF → top-5 → LLM (NO rerank, 5 APIs quá ít)

### Data storage
```
artifacts/
├── docs/
│   ├── chunks.jsonl       # metadata + text
│   ├── faiss.index        # vector index
│   └── bm25.pkl           # BM25 + corpus
└── api/
    ├── schemas.json       # func_code → full APIEntry dict
    ├── faiss.index        # vector index (131 entries)
    ├── bm25.pkl
    └── fuzzy_targets.json # [{id, text}]
```

---

## Next steps (ưu tiên)

1. **rrf.py** — merge retrieval results (independent, small)
2. **Build scripts** (01, 02, 03) — prepare indices
3. **Retriever layers** (doc_retriever, api_retriever)
4. **Reranker** (cross-encoder)
5. **LLM module** (prompts, JSON validator)
6. **Intent classifier** (TF-IDF+LR)
7. **Pipelines** (orchestrate stores + retrievers + LLM)
8. **Data augmentation** (Gemini gen 500 MCQ + 300 API Q&A)
9. **Eval** (run on 100 example, error analysis)
10. **Inference** (617 test, batch embedding, query cache)

---

## Lưu ý quan trọng

- **Fuzzy chỉ cho call_api**, không cho document
- **call_document có filter_fn**, call_api không (không cần)
- **BM25 corpus phải persist** (avoid re-segment)
- **Index file riêng biệt** — không share giữa doc/api
- **5 retrieval strategies** chưa decide, cần eval trên 100 example trước
- **Qwen3-4B thinking OFF** cho cả call_document (CoT trong prompt) lẫn call_api (structured extraction)

---

## Errors fixed

1. ✓ FuzzyStore: import `fuzz.WRatio` thay vì `rf_utils.default_process`
2. ✓ FuzzyStore: target text = Vietnamese (name+description), NOT func_code
3. ✓ config.py: `os.getenv()` Path default bug (cần `str()` wrapper)

---

## Files to open in next session

- `rag/src/retrieval/rrf.py` — tạo mới
- `scripts/02_build_doc_index.py` — tạo mới
- `scripts/03_build_api_index.py` — tạo mới
- `rag/src/retrieval/doc_retriever.py` — tạo mới
- `rag/src/retrieval/api_retriever.py` — tạo mới