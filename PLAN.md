# RAG Chatbot — Tổng hợp thiết kế

## Bài toán

Chatbot xử lý 2 task:

| function_code | Mô tả | function_result |
|---|---|---|
| `call_document` | Trích xuất từ tài liệu PDF | 1 hoặc nhiều đáp án trong A/B/C/D |
| `call_api` | Chọn API đúng và điền params | JSON config đúng format |

**Input**: `id`, `question`, và `note`. Trường `note` chứa 4 lựa chọn MCQ — chỉ dùng trong pipeline `call_document` để inject vào prompt LLM. Format:
```
A, Answer A
 B, Answer B
 C, Answer C
 D, Answer D
```
Parse `note` → dict `{"A": "Answer A", "B": "Answer B", ...}` trước khi build prompt.

**Output**:
```json
{
  "id": "...",
  "function_code": "call_document | call_api",
  "function_result": "A | AB | ... | {\"path\": \"...\", \"body\": {...}}",
  "time_response": 1.23
}
```

---

## Dữ liệu

```
data/                         # (đổi từ LLM/data/)
├── Document_config_data/     # PDF kho tri thức call_document
├── Config_API_RAG.md         # markdown — 131 func_code unique với schema chi tiết
├── Tài liệu config API.xlsx  # Excel source of truth — 2 sheet: Doc_api_for_contest + Doc_alias_for_contest
├── Example_Data_RAG.md       # 100 câu (50 call_doc + 50 call_api) — KHÔNG có function_result
├── example_data.xlsx         # Excel — 3 cột: id, fun_question, note
├── Test_Data_RAG.md          # 617 câu test (chỉ có id + fun_question + note)
└── Test_data.xlsx            # Excel backup
```

**Phát hiện từ đọc data thực tế**:
- `example_data.xlsx` có **3 cột: id, fun_question, note** — KHÔNG có cột `function_result` hay đáp án đúng
- Phân biệt call_doc / call_api **bằng cột `note`**: note = null → call_api; note có A/B/C/D → call_document
- ID range: call_api = 1000–1147, call_document = 701–750
- **131 API** (không phải 136) theo Excel thực tế — Sheet `Doc_api_for_contest`
- Sheet `Doc_alias_for_contest`: 22 alias/enum lookup tables (priorityList, assetGroup, dtmsClass, ...) — dùng để validate params
- `Endpoint config` trong Excel là **JSON blob** chứa: `request`, `example_call`, `required_params`, `optional_params`, `response_schema`
- `structured_output` luôn là `{}` (bỏ qua); `allow_empty_result` luôn là `false` (bỏ qua)
- Câu hỏi call_api là **tiếng Việt thuần** ("Trong năm 2025, TTPMVT có bao nhiêu nhân sự...") — hỏi về PMO dashboards: projects, RA, leakage/defect rate, headcount, revenue
- Câu hỏi call_document là **tiếng Việt MCQ** có reference Public_XXX trong nội dung câu hỏi

**Ý nghĩa với FuzzyStore**:
- Fuzzy matching trên `func_code` (tiếng Anh kỹ thuật) KHÔNG phù hợp vì query là tiếng Việt
- Nên search fuzzy trên `description` hoặc `name` (tiếng Việt) thay vì `func_code`
- Xem chi tiết ở mục [Fuzzy — Thiết kế lại](#fuzzy--thiết-kế-lại) bên dưới

---

## Kiến trúc pipeline

```
Input {id, question}
        │
        ▼
  Intent Classifier (TF-IDF + LR)
  Train trên example_data (100 câu có label sẵn)
  + Gemini Flash gen pseudo-label cho test_data
        │
   ┌────┴────┐
   ▼         ▼
call_doc   call_api
   │         │
RAG pipe  API-RAG pipe
   │         │
  A/B/C/D  JSON config
        │
        ▼
   format JSON output
```

---

## Pipeline 1: call_document (RAG trên PDF)

### Bước 0 — Convert PDF → Markdown (398 files)
- Tool chính: **Marker** (giữ heading structure, bảng, công thức tốt nhất)
- Tool fallback: **PyMuPDF4LLM** (nhanh hơn, dùng khi Marker fail)
- Input: `LLM/data/Document_config_data/*.pdf` (398 files)
- Output: `LLM/data/Document_config_data/output/Public_XXX/main.md`
- **Checkpoint strategy**: convert từng batch 50 file, lưu ngay sau mỗi batch
- **Idempotent**: skip nếu `.md` đã tồn tại → rerun an toàn
- **Error handling**: Nếu Marker fail trên file cụ thể → retry với PyMuPDF4LLM; nếu cả 2 fail → log và skip
- Ước tính thời gian: 2-4h trên Colab T4 (~20-40s/file)

### Bước 1 — Chunking (heading-based + breadcrumb)

Mỗi chunk = 1 heading section, prefix breadcrumb đường dẫn ancestor:

```
[Public_001 > Nội dung chính > Dịch vụ nhà thông minh > Đo điều kiện nhà]

Năm 2010, nhà thông minh được trang bị một bộ cảm biến...
```

Quy tắc kích thước:
- < 80 ký tự → gộp vào parent
- 80–600 ký tự → 1 chunk
- > 600 ký tự → split thêm (RecursiveCharacterTextSplitter, overlap ~80 ký tự), mỗi sub-chunk vẫn giữ breadcrumb prefix

Target: **300–500 ký tự/chunk**

Metadata mỗi chunk:
```python
{
  "doc_id": "Public_001",
  "heading_path": "Nội dung chính > Dịch vụ nhà thông minh > Đo điều kiện nhà",
  "level": 4,
  "chunk_id": "Public_001_012",
  "char_count": 342
}
```

### Bước 2 — Indexing

| Component | Lựa chọn | Lý do |
|---|---|---|
| Dense vector | FAISS | Local, không cần server |
| Embedding | `BAAI/bge-m3` | Multilingual, Vietnamese-aware, 1024-dim |
| Lexical | BM25Okapi (rank-bm25) | Xử lý tên riêng, số liệu, technical terms |
| Persist | FAISS `.index` + BM25 `.pkl` + chunks `.json` lên Google Drive | Không rebuild lại khi thi |

**Lưu ý**: BM25 phải được persist cùng raw texts — lưu pickle để reload không mất index.

**Word segmentation trước khi index BM25** (+10-15% recall):

Tiếng Việt không có khoảng trắng giữa từ ghép — BM25 tách sai nếu không segment:
```
"thư viện dữ liệu API" → ['thư', 'viện', 'dữ', 'liệu', 'API']  ← sai
                       → ['thư_viện', 'dữ_liệu', 'API']          ← đúng
```
Dùng `pyvi` để segment **1 lần offline** khi build index (không ảnh hưởng inference):
```python
from pyvi import ViTokenizer
tokenized = [ViTokenizer.tokenize(text).lower().split() for text in raw_texts]
bm25 = BM25Okapi(tokenized)
```
Query cũng phải segment tương tự trước khi search BM25.

### Bước 3 — Retrieval

**3a — Document-level filter**

- Regex extract `Public_\d+` từ question text
- Nếu tìm thấy → filter FAISS search chỉ trong doc đó
- `note` field KHÔNG dùng để filter — nó chứa các lựa chọn A/B/C/D, sẽ dùng ở Bước 4

**3b — Hybrid Search**
```
BM25(query)   → top 20
Vector(query) → top 20
      ↓
  RRF Fusion: score(d) = Σ 1/(60 + rank_i(d))
      ↓
  top 20 merged
```

RRF tốt hơn weighted sum vì BM25 score và cosine similarity ở 2 thang đo khác nhau.

**3c — Cross-encoder Reranker**
```
top 20 → BAAI/bge-reranker-v2-m3 → top 5
```

### Bước 4 — LLM Answer Selection

Top 5 chunks + question + options (parsed từ `note`) → LLM → chọn A/B/C/D.

**Parse `note` trước khi build prompt**:
```python
# note = "A, Answer A\n B, Answer B\n C, Answer C\n D, Answer D"
options = {}
for line in note.strip().split("\n"):
    line = line.strip()
    if line and "," in line:
        key, val = line.split(",", 1)
        options[key.strip()] = val.strip()
# → {"A": "Answer A", "B": "Answer B", "C": "Answer C", "D": "Answer D"}
```

**Prompt dùng CoT** (0ms cost, +1-2% accuracy — buộc LLM lập luận trước khi chọn):

```
Dựa vào các đoạn tài liệu dưới đây, hãy lập luận từng bước rồi chọn đáp án đúng.

[1] {chunk_1}
[2] {chunk_2}
...

Câu hỏi: {question}
A. {options["A"]}   B. {options["B"]}   C. {options["C"]}   D. {options["D"]}

Hãy lập luận từng bước dựa vào tài liệu, rồi trả lời bằng chữ cái duy nhất.
Đáp án:
```

Thinking mode: **tắt** — Qwen3-4B vẫn suy luận trong output text mà không cần thinking block.

---

## Pipeline 2: call_api (Hybrid retrieval + LLM chọn & fill)

Với 136 API entries, description ngắn → **không chunk**. Mỗi API = 1 document.
LLM nhận **top-5 candidates** và tự chọn + fill params trong 1 lần gọi (tiết kiệm code, tận dụng semantic của LLM).

```
Tầng 1: Hybrid retrieval (Fuzzy + BM25 + FAISS) → RRF → top-5 func_code
Tầng 2: Inject 5 schemas vào prompt LLM → LLM chọn + fill params → JSON
Tầng 3: Validate JSON (3-tier fallback)
```

### Bước 1 — Index API (offline, 1 lần)
- Source: `data/Tài liệu config API.xlsx` — Sheet `Doc_api_for_contest` (131 entries)
- Parse ra 131 entries, mỗi entry có: `func_code`, `name`, `description`, `Example question`, `Endpoint config` (JSON)
- Mỗi API = 1 document embed (concat `name + description + Example question`)
- Build **3 indices song song**:
  - **FAISS**: 131 vectors × 1024-dim (bge-m3) → `api_faiss.index`
  - **BM25**: pyvi segment trên `name + description + Example question` → `api_bm25.pkl`
  - **Fuzzy target list**: `[{id: func_code, text: name + " " + description}]` — **tiếng Việt**, không phải func_code
- Lưu song song: dict `func_code → full_schema` JSON để lookup O(1)
- Lưu thêm: Sheet `Doc_alias_for_contest` → `api_aliases.json` để validate enum params

### Bước 2 — Retrieve top-5 candidates
Chạy 3 nguồn **song song**:
- **Fuzzy** (RapidFuzz WRatio) trên `name + description` (tiếng Việt) → top-5 + score
  - Bắt khi user gõ gần đúng tên API bằng tiếng Việt (vd: "nhân sự làm việc" → "Lấy số nhân sự đang làm việc")
  - **KHÔNG** fuzzy trên func_code (vì query là tiếng Việt, không phải tiếng Anh kỹ thuật)
- **BM25** trên `name + description + Example question` (pyvi tokenized) → top-5 + score
  - Bắt từ khóa chính xác tiếng Việt ("leakage rate", "RA", "SLSX")
- **FAISS** trên `name + description + Example question` embedding (bge-m3) → top-5 + score
  - Bắt semantic khi từ vựng khác nhau (vd: "doanh thu" ↔ "revenue", "nhân sự" ↔ "headcount")

→ **RRF fusion** 3 nguồn → **top-5 func_code**

### Bước 3 — LLM chọn + fill params (1 LLM call)
Inject 5 schemas vào prompt, LLM tự quyết định API nào đúng nhất và điền params:

```
Câu hỏi: {question}

Dưới đây là 5 API có thể phù hợp. Hãy chọn API đúng nhất và điền params từ câu hỏi:

[1] func_code: get_total_projects_by_unit
    Mô tả: Lấy tổng số dự án theo đơn vị
    Path: /api/v1/dashboard/project-overview/organization
    Required: projectStatus (List<String>), projectType (List<String>),
              fromDate (yyyy-mm-dd), toDate (yyyy-mm-dd)
    Optional: organization (List<String>), isCompany (Boolean)
    Giá trị hợp lệ: projectStatus ∈ [in-progress, hold, closed, presale, open]
                   projectType ∈ [T&M, presales, odc/osdc, package]

[2] func_code: ...
[3] func_code: ...
[4] func_code: ...
[5] func_code: ...

Trả về JSON đúng format sau (không giải thích thêm):
{
  "func_code": "<chọn 1 trong 5 func_code ở trên>",
  "path": "<path tương ứng>",
  "body": { ... }
}
```

Model: Qwen3-4B (4-bit, thinking **OFF**).

**Lý do chọn top-5 thay vì top-1/3**:
- LLM có nhiều context hơn để phân biệt API gần giống nhau (vd: `get_defect_rate_cumulative` vs `get_defect_rate_norm`)
- Bỏ được logic code phức tạp chọn top-1 bằng threshold/tie-breaking → LLM quyết định semantic tốt hơn
- 5 schemas × ~50 dòng = ~700 tokens, Qwen3-4B (context 32k) thừa sức
- Chỉ 1 LLM call, chậm hơn ~1s so với top-1 nhưng đổi lại accuracy cao hơn

### Bước 4 — Validation layer 3 tầng (tránh 0 điểm do JSON malformed)
1. **Strict parse**: `json.loads(raw_output)` → validate `func_code` ∈ top-5
2. **Regex fallback**: Nếu parse fail, extract `{...}` block đầu tiên bằng regex → retry parse
3. **Best-effort**: Nếu vẫn fail, dùng top-1 từ RRF + body rỗng (vẫn chấm điểm phần path)

Sau parse thành công, validate:
- `func_code` có trong top-5 không (tránh LLM hallucinate)
- Required params có đủ không
- Type đúng không (Date "yyyy-mm-dd", List<String>, Boolean...)
- Path match với func_code đã chọn

**Nguyên tắc**:
- Không chunk API (description ngắn, chunking kém hiệu quả hơn full document match)
- Không dùng reranker (136 entries quá ít, RRF 3 nguồn đủ rồi)
- Không dùng thinking ON (output structured, không cần reasoning phức tạp)
- LLM chọn + fill trong 1 call — tiết kiệm code, accuracy cao hơn logic rule-based

---

## Data Augmentation (Gen synthetic data)

### Vì sao cần
100 labeled examples (50+50) quá ít để:
- Train classifier robust
- Eval pipeline accuracy trước khi chạy 617 test
- Phát hiện failure modes sớm

### Chiến lược gen

**1. Gen MCQ cho call_document** (~500 câu)
- Với mỗi chunk "thú vị" (>300 chars, có số liệu/khái niệm/định nghĩa):
  Gemini Flash gen 1 câu MCQ + 4 đáp án A/B/C/D + đáp án đúng
- Output: `LLM/data/synthetic/doc_qa.jsonl`
- Mục đích: Eval set cho RAG pipeline

**2. Gen call_api questions** (~300 câu)
- Với mỗi trong 136 func_code + example_call có sẵn:
  Gemini Flash gen 2-3 variations câu hỏi tự nhiên (diễn đạt khác nhau)
  Ground truth = `example_call` JSON có sẵn trong Config_API_RAG.md
- Output: `LLM/data/synthetic/api_qa.jsonl`
- Mục đích: Eval set cho API pipeline + augment classifier training

**3. Chia train/eval**
- **Classifier training**: 100 real + 500 synthetic = 600 samples
- **Pipeline eval**: 100 real (held-out, KHÔNG đưa vào train)

### Rate limit handling
- Gemini Flash free: 15 RPM, 1500/day
- Batch request, sleep 4s giữa calls → ~3 giờ để gen 800 samples
- Retry 3 lần với exponential backoff nếu fail

---

## Intent Classifier

- **Training data**: 600 samples (100 real + 500 synthetic từ bước trên)
- **Model**: TF-IDF + Logistic Regression (không rule-based, không fallback)
- **Feature engineering**: Thêm signal "có chứa A/B/C/D hoặc 4 options" → boost call_document
- **Persist**: lưu `.pkl` cùng index files lên Google Drive

---

## Model Stack

| Role | Model | VRAM base | VRAM runtime |
|---|---|---|---|
| Embedding (dùng chung doc + API) | `BAAI/bge-m3` | ~1GB | +0.5GB (batch) |
| Reranker | `BAAI/bge-reranker-v2-m3` | ~1.1GB | +0.3GB (cross-attention) |
| LLM | **Qwen3-4B (4-bit)** | ~2.5GB | +1-2GB (KV cache cho 2k-4k context) |
| **Tổng** | | **~4.6GB base** | **~7-8GB thực tế** |

**T4 Colab Free**: 15GB VRAM → đủ buffer cho ~7-8GB thực tế ✓

**Qwen3-4B (4-bit)**:
- Thinking mode: **tắt** cho cả `call_document` lẫn `call_api`
- `call_document`: CoT trong prompt text, không cần thinking block
- `call_api`: output là structured JSON extraction, không cần reasoning phức tạp

---

## Môi trường chạy — Google Colab

**Tách 2 giai đoạn bắt buộc:**

```
Giai đoạn 1 — OFFLINE (chạy trước, lưu Google Drive):
  PDF → Marker → markdown → chunk (pyvi segment) → embed → FAISS doc index
                                                          → BM25 doc pickle
                                                          → chunks metadata JSON
  Config_API_RAG.md → parse 136 entries → embed (name+desc+example) → FAISS API index
                                        → BM25 API pickle (pyvi segment)
                                        → func_code → full_schema dict JSON
                                        → fuzzy target list (func_code + name)
  example_data + Gemini labels → TF-IDF+LR → classifier.pkl

Giai đoạn 2 — INFERENCE (khi thi trên Colab):
  Load từ Drive → classifier → RAG / API-lookup → LLM → output JSON
  (không rebuild index)
  Query caching: query_text → embedding (skip re-encode nếu câu giống nhau)
```

**Query caching** (free performance khi chạy batch 617 câu):
```python
query_cache = {}

def get_embedding(text):
    if text not in query_cache:
        query_cache[text] = model.encode(text)
    return query_cache[text]
```

---

## Eval Strategy — Validate trước khi chạy 617 test

### Giai đoạn validate (BẮT BUỘC)
1. Chạy pipeline hoàn chỉnh trên 100 example (50 call_doc + 50 call_api)
2. Đo metrics:
   - Classifier accuracy (call_doc vs call_api)
   - call_document: exact match rate (A/AB/ABC match với đáp án đúng)
   - call_api: JSON validity rate + path match rate + body match rate
   - Avg `time_response` per question (mục tiêu < 15s)
3. **Nếu accuracy tổng < 70%: KHÔNG chạy 617 test**, debug trước

### Logging (mỗi câu bắt buộc log)
- Classifier confidence + predicted label
- Top-5 chunks retrieved (chunk_id + score)
- Raw LLM output (trước parse)
- Parsed output
- `time_response` breakdown (embed / retrieve / rerank / LLM)

### Error analysis — bucket errors theo tầng:
- `classifier_wrong`: Intent sai → sửa feature engineering
- `retrieval_miss`: Top-5 không chứa chunk đúng → sửa chunking hoặc hybrid weights
- `llm_wrong`: Chunk đúng nhưng LLM chọn sai → sửa prompt
- `json_invalid`: Parse fail → sửa validation layer

Focus fix bucket LỚN NHẤT trước, không dàn trải.

---

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Marker fail trên PDF phức tạp | Fallback PyMuPDF4LLM; skip file nếu cả 2 fail |
| Gemini Flash rate limit khi gen 800 samples | Batch + sleep 4s; retry 3 lần exponential backoff |
| Classifier confuse call_doc vs call_api | Feature: regex detect "A/B/C/D" pattern → call_doc signal |
| JSON parse fail trên call_api | 3-tier: strict parse → regex extract → best-effort |
| 617 câu × 4s = ~40 phút, có thể timeout Colab | Batch embedding; parallel retrieval (threading) |
| Accuracy < 70% trên eval set | KHÔNG chạy 617 test — debug error bucket lớn nhất |
| PDF conversion 2-4h crash giữa chừng | Checkpoint từng batch 50 file; idempotent skip |

---

## Thứ tự implementation

1. **PDF conversion**: Marker (checkpoint mỗi 50 file) → fallback PyMuPDF4LLM
2. **Chunking**: heading + breadcrumb + pyvi segment, persist chunks JSON
3. **Index documents**: FAISS (bge-m3) + BM25 (pyvi tokenized) → Drive
4. **Parse + Index API**: `Config_API_RAG.md` → 136 schemas dict + FAISS + BM25 + fuzzy list
5. **[MỚI] Data augmentation**: Gen 500 MCQ + 300 API Q&A bằng Gemini Flash
6. **Intent Classifier**: train TF-IDF+LR trên 600 samples, có feature "A/B/C/D pattern"
7. **RAG pipeline (call_document)**: hybrid retrieval + reranker + CoT prompt + Qwen3-4B
8. **API pipeline (call_api)**: Fuzzy+BM25+FAISS → RRF top-5 → LLM chọn+fill → 3-tier JSON validation
9. **[MỚI] Eval trên 100 example**: log đầy đủ → error analysis → iterate fix
10. **Run inference 617 test**: batch embedding, query cache → output JSON

---

## Những thứ đã bỏ / không dùng

- `LLM/ai_agent/` folder cũ → **viết lại từ đầu hoàn toàn** (quyết định của user)
- `training_data_update/`, `public_test_data/` → **thay bằng `LLM/data/`**
- References `API_config_data/`, `example_data/`, `test_data/` folders → **không tồn tại** (data là Markdown + Excel)
- Rule-based intent (keyword matching) → không dùng (ngoại trừ feature "A/B/C/D pattern" làm signal phụ)
- Weighted sum hybrid (code cũ) → thay bằng RRF
- BM25 không persist (lỗi code cũ) → fix bằng cách lưu pickle
- call_api = gọi thẳng local model (cũ) → **thay bằng hybrid retrieval (Fuzzy+BM25+FAISS) + LLM chọn&fill**
- Logic code phức tạp chọn top-1 (threshold, tie-breaking) → LLM tự chọn từ top-5, ít code hơn
- Chunking API → bỏ (description ngắn, chunking kém hiệu quả hơn full match)
- Qwen3-4B thinking ON cho call_api (tốn 8-15s không cần) → OFF, structured extraction là đủ
- **Fuzzy trên `func_code`** → bỏ. Query là tiếng Việt, không ai gõ "get_defect_rate_monthly". Thay bằng fuzzy trên `name + description` (tiếng Việt).
- **`Config_API_RAG.md` làm source** → dùng `Tài liệu config API.xlsx` thay thế (structured hơn, dễ parse, có Sheet alias)
- 136 API → thực tế **131 API** theo Excel
