# Architecture — Cấu trúc code, modules, và data flow

> Tài liệu này mô tả **cấu trúc folder, trách nhiệm từng file, và flow work** của hệ thống RAG chatbot. Đọc song song với `PLAN.md` (thiết kế thuật toán).

---

## 1. Nguyên tắc thiết kế

1. **Tách offline vs online**: Build index, train classifier → chạy 1 lần lưu Drive. Inference chỉ load, không rebuild.
2. **Single Responsibility**: Mỗi module 1 trách nhiệm duy nhất.
3. **Config tập trung**: `config.py` ở root, tất cả module import từ đây. Không hardcode path.
4. **Phân vùng theo người**: `rag/` (người B), `classifier/` (người C), `shared/` (dùng chung) → ít git conflict.
5. **Idempotent scripts**: Chạy lại không bị hỏng, skip nếu artifact đã tồn tại.

---

## 2. Cấu trúc folder tổng thể

```
Viettel_RAG/
├── PLAN.md
├── ARCHITECTURE.md
├── config.py                         # [SHARED] Config tập trung — paths, models, hyperparams
├── requirements.txt                  # Python deps chung
│
├── data/                             # [RAW] Data từ ban tổ chức — KHÔNG SỬA
│   ├── Document_config_data/         # 398 PDF gốc
│   ├── Config_API_RAG.md             # API schemas (136 func_code)
│   ├── Example_Data_RAG.md           # 100 labeled questions
│   ├── Test_Data_RAG.md              # 617 test questions
│   └── *.xlsx
│
├── artifacts/                        # [BUILT] Index + model artifacts → persist lên Drive
│   ├── docs/
│   │   ├── chunks.jsonl
│   │   ├── faiss.index
│   │   └── bm25.pkl
│   ├── api/
│   │   ├── schemas.json
│   │   ├── faiss.index
│   │   ├── bm25.pkl
│   │   └── fuzzy_targets.json
│   └── classifier/
│       └── intent.pkl
│
├── synthetic/                        # [BUILT] Gen từ Gemini Flash
│   ├── doc_qa.jsonl
│   └── api_qa.jsonl
│
├── outputs/                          # [BUILT] Kết quả chạy
│   ├── eval/
│   │   ├── predictions.jsonl
│   │   ├── metrics.json
│   │   └── errors.jsonl
│   └── submission/
│       └── result.json
│
├── logs/
│
├── shared/                           # [SHARED] Code dùng chung — cả 3 người đều import
│   ├── __init__.py
│   ├── types.py                      # Dataclasses: Question, Chunk, APIEntry, RetrievalHit
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       ├── timer.py
│       ├── vi_text.py
│       └── io.py
│
├── rag/                              # [CODE] Người B — RAG pipeline
│   ├── requirements.txt
│   ├── .env.example
│   ├── scripts/
│   │   ├── 02_build_doc_index.py
│   │   ├── 03_build_api_index.py
│   │   ├── 04_gen_synthetic.py
│   │   ├── 06_eval.py
│   │   └── 07_run_inference.py
│   └── src/
│       ├── __init__.py
│       ├── chunking/
│       │   └── heading_chunker.py
│       ├── indexing/
│       │   ├── embedder.py
│       │   ├── faiss_store.py
│       │   ├── bm25_store.py
│       │   └── fuzzy_store.py
│       ├── retrieval/
│       │   ├── rrf.py
│       │   ├── reranker.py
│       │   ├── doc_retriever.py
│       │   └── api_retriever.py
│       ├── llm/
│       │   ├── qwen.py
│       │   ├── prompts.py
│       │   └── json_validator.py
│       ├── pipeline/
│       │   ├── doc_pipeline.py
│       │   ├── api_pipeline.py
│       │   └── orchestrator.py
│       ├── augmentation/
│       │   ├── gemini_client.py
│       │   ├── gen_doc_mcq.py
│       │   └── gen_api_q.py
│       └── eval/
│           ├── metrics.py
│           └── analyzer.py
│
└── intent/                       # [CODE] Người C — Intent classifier
    ├── scripts/
    │   └── 05_train_classifier.py
    └── src/
        ├── __init__.py
        ├── md_parser.py
        ├── features.py
        └── classifier.py
```

---

## 3. `config.py` — Config tập trung

Nằm ở root `Viettel_RAG/`. `ROOT = Path(__file__).parent` — đơn giản, không đếm `.parent`.

```python
import os
from pathlib import Path

ROOT = Path(__file__).parent  # Viettel_RAG/

# Raw data
DATA_DIR       = Path(os.getenv("DATA_DIR",       ROOT / "data"))
MINERU_OUT_DIR = Path(os.getenv("MINERU_OUT_DIR", ROOT / "training_data_update" / "output"))

API_CONFIG_MD = DATA_DIR / "Config_API_RAG.md"
EXAMPLE_MD    = DATA_DIR / "Example_Data_RAG.md"
TEST_MD       = DATA_DIR / "Test_Data_RAG.md"

# Artifacts
ARTIFACTS_DIR = Path(os.getenv("ARTIFACTS_DIR", ROOT / "artifacts"))
SYNTHETIC_DIR = Path(os.getenv("SYNTHETIC_DIR", ROOT / "synthetic"))
OUTPUTS_DIR   = Path(os.getenv("OUTPUTS_DIR",   ROOT / "outputs"))
LOGS_DIR      = Path(os.getenv("LOGS_DIR",      ROOT / "logs"))

DOC_CHUNKS  = ARTIFACTS_DIR / "docs" / "chunks.jsonl"
DOC_FAISS   = ARTIFACTS_DIR / "docs" / "faiss.index"
DOC_BM25    = ARTIFACTS_DIR / "docs" / "bm25.pkl"
API_SCHEMAS = ARTIFACTS_DIR / "api" / "schemas.json"
API_FAISS   = ARTIFACTS_DIR / "api" / "faiss.index"
API_BM25    = ARTIFACTS_DIR / "api" / "bm25.pkl"
API_FUZZY   = ARTIFACTS_DIR / "api" / "fuzzy_targets.json"
CLASSIFIER  = ARTIFACTS_DIR / "classifier" / "intent.pkl"

# Models
EMBED_MODEL      = "BAAI/bge-m3"
RERANK_MODEL     = "BAAI/bge-reranker-v2-m3"
LLM_MODEL        = "Qwen/Qwen3-4B"
LLM_QUANTIZATION = "4bit"

# Chunking (word-based)
CHUNK_MIN_WORDS     = 5
CHUNK_MAX_WORDS     = 120
CHUNK_OVERLAP_WORDS = 15

# Retrieval
BM25_TOP_K         = 20
FAISS_TOP_K        = 20
RRF_K              = 60
RERANK_TOP_K       = 3
API_RETRIEVE_TOP_K = 5

# LLM
LLM_MAX_NEW_TOKENS = 512
LLM_THINKING_MODE  = False
LLM_TEMPERATURE    = 0.0

# Gemini
GEMINI_MODEL       = "gemini-1.5-flash"
GEMINI_SLEEP       = 4.0
GEMINI_MAX_RETRIES = 3

# Eval
EVAL_ACCURACY_THRESHOLD = 0.70
TIME_RESPONSE_TARGET    = 15.0
```

**Khi chạy Colab**: set 1 dòng trước khi import:
```python
import os
os.environ["ROOT"] = "/content/drive/MyDrive/Viettel_RAG"
```

**Import trong mọi module**:
```python
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[N]))  # trỏ về root
import config
from shared.types import Question, Chunk
```

---

## 4. `shared/` — Code dùng chung

Cả 3 người đều import. **Ai cũng có thể đề xuất thay đổi, nhưng phải thông báo team trước.**

### `shared/types.py` — Dataclasses
```python
@dataclass
class Question:
    id: int
    question: str
    note: str | None = None       # A/B/C/D options cho MCQ

@dataclass
class Chunk:
    chunk_id: str                 # "Public_001_012"
    doc_id: str                   # "Public_001"
    heading_path: str             # breadcrumb
    level: int
    char_count: int
    text: str                     # text có prefix breadcrumb

@dataclass
class APIEntry:
    func_code: str
    name: str
    description: str
    example_question: str
    path: str
    required_params: list[dict]
    optional_params: list[dict]
    response_schema: dict
    example_body: dict

@dataclass
class RetrievalHit:
    id: str                       # chunk_id hoặc func_code
    score: float
    source: str                   # "bm25" | "faiss" | "fuzzy"
    rank: int
```

### `shared/utils/`
- `logger.py` — `get_logger(name)` → JSON logger ghi ra `LOGS_DIR`
- `timer.py` — context manager `Timer()` đo wall clock
- `vi_text.py` — `segment(text) -> list[str]`, LRU cache 10k entries
- `io.py` — `load/save json, jsonl, pickle`; atomic write

---

## 5. `rag/` — RAG pipeline (người B)

### 5.1. `src/chunking/heading_chunker.py`
- Input: path tới `Public_XXX/main.md` từ `MINERU_OUT_DIR`
- Output: `list[Chunk]`
- Logic: parse heading tree → breadcrumb → split nếu > 600 chars

### 5.2. `src/indexing/`
- `embedder.py` — bge-m3 wrapper, batch encode, L2 normalize
- `faiss_store.py` — build/save/load FAISS IndexFlatIP, `search(query_vec, top_k, filter_fn)`
- `bm25_store.py` — pyvi segment + BM25Okapi, persist cả corpus, `search(query, top_k)`
- `fuzzy_store.py` — RapidFuzz WRatio trên func_code + name

### 5.3. `src/retrieval/`
- `rrf.py` — `rrf_fusion(results_per_source, k=60, top_k) -> list[RetrievalHit]`
- `reranker.py` — bge-reranker-v2-m3
- `doc_retriever.py` — BM25+FAISS → RRF → Reranker top-5; regex extract `Public_\d+`
- `api_retriever.py` — Fuzzy+BM25+FAISS song song → RRF top-5

### 5.4. `src/llm/`
- `qwen.py` — Qwen3-4B 4-bit singleton, `generate(prompt, thinking=False) -> str`
- `prompts.py` — `build_doc_prompt(chunks, question, options)`, `build_api_prompt(question, candidates)`
- `json_validator.py` — 3-tier: strict → regex extract → best-effort

### 5.5. `src/pipeline/`
- `doc_pipeline.py` — retrieve → parse note → CoT prompt → extract A/B/C/D
- `api_pipeline.py` — retrieve → 5 schemas prompt → 3-tier JSON parse
- `orchestrator.py` — classify → route → `run_batch()`

---

## 6. `classifier/` — Intent Classifier (người C)

- `src/md_parser.py` — parse Example_Data_RAG.md, Test_Data_RAG.md, Config_API_RAG.md
- `src/features.py` — `has_abcd_pattern`, `has_date_range`, `has_public_ref`
- `src/classifier.py` — TF-IDF + LR + FeatureUnion, `predict(question) -> (label, confidence)`

---

## 7. Data flow

### Offline (chạy 1 lần)
```
training_data_update/output/Public_XXX/main.md
    → heading_chunker → chunks.jsonl
    → embedder + faiss_store → docs/faiss.index
    → bm25_store (pyvi) → docs/bm25.pkl

data/Config_API_RAG.md
    → md_parser → 136 APIEntry
    → schemas.json, faiss.index, bm25.pkl, fuzzy_targets.json

data/Example_Data_RAG.md + synthetic/*.jsonl
    → IntentClassifier.train → classifier/intent.pkl
```

### Inference (mỗi question)
```
Question {id, question, note?}
    → IntentClassifier.predict → "call_document" | "call_api"
    → DocPipeline hoặc APIPipeline
    → {id, function_code, function_result, time_response}
```

---

## 8. Thứ tự implement

```
Foundation (làm trước):
[ ] config.py                         ← đã có
[ ] shared/types.py
[ ] shared/utils/ (logger, timer, io, vi_text)

Data parsing (người C):
[ ] classifier/src/md_parser.py

Indexing — rag/:
[ ] rag/src/indexing/embedder.py
[ ] rag/src/indexing/faiss_store.py
[ ] rag/src/indexing/bm25_store.py
[ ] rag/src/indexing/fuzzy_store.py
[ ] rag/src/chunking/heading_chunker.py
[ ] rag/scripts/02_build_doc_index.py
[ ] rag/scripts/03_build_api_index.py

Retrieval ⭐:
[ ] rag/src/retrieval/rrf.py
[ ] rag/src/retrieval/reranker.py
[ ] rag/src/retrieval/doc_retriever.py
[ ] rag/src/retrieval/api_retriever.py

LLM ⭐:
[ ] rag/src/llm/qwen.py
[ ] rag/src/llm/prompts.py
[ ] rag/src/llm/json_validator.py

Intent (người C):
[ ] classifier/src/features.py
[ ] classifier/src/classifier.py
[ ] classifier/scripts/05_train_classifier.py

Pipeline ⭐:
[ ] rag/src/pipeline/doc_pipeline.py
[ ] rag/src/pipeline/api_pipeline.py
[ ] rag/src/pipeline/orchestrator.py

Eval + inference:
[ ] rag/scripts/06_eval.py
[ ] rag/scripts/07_run_inference.py
```

---

## 9. Quy ước

- Không sửa `data/`, `training_data_update/`, `public_test_data/`
- `shared/` chỉ chứa code dùng chung — không để logic RAG hay classifier vào đây
- Mọi script chạy từ root `Viettel_RAG/` hoặc set `PROJECT_ROOT` env var khi Colab
- Pipeline level: catch exception → log → best-effort output (không để crash mất điểm)
