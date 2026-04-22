# RAG Chatbot — Tổng hợp thiết kế

## Bài toán

Chatbot xử lý 2 task:

| function_code | Mô tả | function_result |
|---|---|---|
| `call_document` | Trích xuất từ tài liệu PDF/MD | 1 hoặc nhiều đáp án trong A/B/C/D |
| `call_api` | Gọi local model trực tiếp | Raw response từ model (không qua RAG) |

**Input**: chỉ dùng `id` và `question`. Trường `note` chỉ được dùng SAU KHI đã classify ra `call_document`.

**Output**:
```json
{
  "id": "...",
  "function_code": "call_document | call_api",
  "function_result": "A | AB | ... | <raw response>",
  "time_response": 1.23
}
```

---

## Dữ liệu

| Nguồn | Nội dung | Trạng thái |
|---|---|---|
| `training_data_update/output/Public_001–292/main.md` | 292 file markdown đã convert từ PDF | Sẵn sàng |
| `public_test_data/Public_285–396/*.pdf` | ~50 PDF chưa convert | Cần convert |
| `training_data_update/input/question.csv` | 1529 câu hỏi (train/public_test/private_test), không có cột Answer | Có sẵn |
| `public_test_data/question.xlsx` | 310 câu test (Q, A, B, C, D) — đây là input chính khi thi | Có sẵn |
| API data | Không có — call_api = gọi thẳng local model | Không cần |

---

## Kiến trúc pipeline

```
Input {id, question}
        │
        ▼
  Intent Classifier  ←── train sau (TF-IDF+LR hoặc embedding centroid)
  (ML, không rule-based)  ←── dùng GPT/Gemini gen pseudo-label trước
        │
   ┌────┴────┐
   ▼         ▼
call_doc   call_api
   │         │
RAG pipe  Local Model
   │      (direct, no RAG)
   ▼         ▼
  A/B/C/D  raw text
        │
        ▼
   format JSON output
```

---

## RAG Pipeline (call_document) — Đã chốt

### Bước 0 — Convert PDF còn thiếu
- Các PDF trong `public_test_data/` (Public_285–396) cần convert sang markdown
- Tool: **Marker** hoặc **PyMuPDF4LLM**
- Output đưa vào chung corpus với 292 file đã có

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

**Lưu ý**: BM25 phải được persist cùng raw texts — đây là lỗi của code cũ (mất BM25 sau khi reload FAISS).

### Bước 3 — Retrieval

**3a — Document-level filter (entity extraction, không phải rule-based)**

- Regex extract `Public_\d+` từ question text
- Nếu tìm thấy → filter FAISS search chỉ trong doc đó
- Nếu có `note` field → ưu tiên dùng note để filter

**3b — Hybrid Search**
```
BM25(query)   → top 20
Vector(query) → top 20
      ↓
  RRF Fusion: score(d) = Σ 1/(60 + rank_i(d))
      ↓
  top 20 merged
```

RRF tốt hơn weighted sum vì BM25 score và cosine similarity ở 2 thang đo khác nhau — không cần normalize thủ công.

**3c — Cross-encoder Reranker**
```
top 20 → BAAI/bge-reranker-v2-m3 → top 5
```

### Bước 4 — LLM Answer Selection

Top 5 chunks + question + options → LLM → chọn A/B/C/D:

```
Dựa vào các đoạn tài liệu dưới đây, chọn đáp án đúng.

[1] {chunk_1}
[2] {chunk_2}
...

Câu hỏi: {question}
A. {A}   B. {B}   C. {C}   D. {D}

Trả lời bằng chữ cái đáp án. Nếu nhiều đáp án đúng, liệt kê tất cả (ví dụ: AB).
```

---

## Model stack — Đã chốt

| Role | Model | VRAM |
|---|---|---|
| Embedding | `BAAI/bge-m3` | ~1GB |
| Reranker | `BAAI/bge-reranker-v2-m3` | ~1.1GB |
| LLM | **Qwen3-4B (4-bit)** | ~2.5GB |
| **Tổng** | | **~4.6GB** (T4 15GB ✓) |

**Qwen3-4B (4-bit) được chọn thay vì Qwen2.5-7B-Instruct (4-bit) vì:**
- Thế hệ mới hơn (Apr 2025), reasoning tốt hơn dù ít params hơn
- Tiết kiệm ~2GB VRAM
- Inference nhanh hơn → time_response tốt hơn
- Có thinking mode: **tắt** (`/no_think`) cho `call_document`, **bật** cho `call_api`

### Colab Free compatibility
- T4 GPU 15GB VRAM + 4-bit quantization → **~4.6GB tổng VRAM** → **Chạy được ✓**
- Đủ buffer an toàn, không cần upgrade

### Finetune strategy
- **Phase 1 (hiện tại)**: Không finetune — dùng prompt engineering + RAG
- **Phase 2 (nếu accuracy < target)**: Finetune trên Kaggle (~2-4h với 1000 ví dụ)
  - Data: question.csv (1001 train) + nhãn từ GPT/Gemini
  - Output: lưu checkpoint, load vào model.py khi inference
  - Không cần finetune embedding/reranker

---

## Môi trường chạy — Google Colab

**Tách 2 giai đoạn bắt buộc:**

```
Giai đoạn 1 — OFFLINE (chạy trước, lưu Google Drive):
  markdown files → chunk → embed → FAISS index
                                 → BM25 pickle
                                 → chunks metadata JSON

Giai đoạn 2 — INFERENCE (khi thi trên Colab):
  Load từ Drive → retrieval → LLM → output JSON
  (không rebuild index)
```

---

## Intent Classifier — Kế hoạch (chưa implement)

- Dùng GPT/Gemini gen pseudo-label cho 1529 câu trong `question.csv`
- Train TF-IDF + Logistic Regression (hoặc embedding centroid)
- **Không dùng rule-based** (yêu cầu của giáo viên)
- **Không có fallback** — luôn chọn class có score cao hơn
- Hiện tại chưa có data cho `call_api` class — cần bổ sung khi có

---

## Thứ tự implementation

1. Chunking module (heading + breadcrumb, persist chunks)
2. FAISS + BM25 indexing (persist cả 2 lên Drive)
3. Hybrid retrieval (RRF)
4. Reranker wrapper
5. LLM answer selection (Qwen3-4B)
6. Pipeline wrapper (đọc input xlsx → chạy → ghi output JSON)
7. Intent classifier (sau khi có labeled data)

---

## Những thứ đã bỏ / không dùng

- `ai_agent/` folder cũ → **xóa hoặc bỏ qua hoàn toàn, viết lại từ đầu**
- Rule-based intent (keyword matching) → không dùng
- Weighted sum hybrid (code cũ) → thay bằng RRF
- BM25 không persist (lỗi code cũ) → fix bằng cách lưu pickle
- Embedding model không nhất quán (code cũ dùng 2 model khác nhau) → chỉ dùng `BAAI/bge-m3`
