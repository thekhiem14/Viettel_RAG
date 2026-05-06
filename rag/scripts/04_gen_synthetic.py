"""Gen synthetic data bằng Gemini Flash:
  - 500 MCQ cho call_document (từ chunks)
  - 300 câu hỏi cho call_api (từ API schemas)

Usage:
    python rag/scripts/04_gen_synthetic.py --mode doc   # gen MCQ
    python rag/scripts/04_gen_synthetic.py --mode api   # gen API Q&A
    python rag/scripts/04_gen_synthetic.py              # cả 2

Output:
    synthetic/doc_qa.jsonl  — {question, options: {A,B,C,D}, answer, doc_id, chunk_id}
    synthetic/api_qa.jsonl  — {question, func_code, label: "call_api"}
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import config
from shared.utils.io import load_jsonl, save_jsonl
from shared.utils.logger import get_logger
from shared.types import Chunk

logger = get_logger("04_gen_synthetic", config.LOGS_DIR)


def _gemini_client():
    import google.generativeai as genai
    genai.configure(api_key=config.GEMINI_API_KEY)
    return genai.GenerativeModel(config.GEMINI_MODEL)


def _call_gemini(model, prompt: str, retries: int = 3) -> str | None:
    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.warning("gemini_retry", extra={"attempt": attempt, "error": str(e)})
            time.sleep(2 ** attempt)
    return None


def gen_doc_mcq(n_per_chunk: int = 1, max_chunks: int = 500) -> None:
    """Gen MCQ từ document chunks."""
    config.ensure_dirs()
    out_path = config.SYNTHETIC_DIR / "doc_qa.jsonl"

    if not config.DOC_CHUNKS.exists():
        raise FileNotFoundError(f"chunks.jsonl not found: {config.DOC_CHUNKS}")

    model = _gemini_client()
    results = []
    count = 0

    for chunk_dict in load_jsonl(config.DOC_CHUNKS):
        if count >= max_chunks:
            break
        chunk = Chunk(**chunk_dict)
        if chunk.char_count < 300:
            continue

        prompt = f"""Dựa vào đoạn tài liệu dưới đây, hãy tạo 1 câu hỏi trắc nghiệm (MCQ) với 4 lựa chọn A/B/C/D.

Tài liệu:
{chunk.text[:800]}

Yêu cầu:
- Câu hỏi phải dựa hoàn toàn vào nội dung tài liệu
- Chỉ có 1 đáp án đúng
- Trả về JSON theo format: {{"question": "...", "A": "...", "B": "...", "C": "...", "D": "...", "answer": "A"}}
- Không giải thích thêm"""

        raw = _call_gemini(model, prompt)
        if raw:
            try:
                import re
                m = re.search(r"\{[\s\S]*\}", raw)
                if m:
                    data = json.loads(m.group())
                    results.append({
                        "question": data.get("question", ""),
                        "options": {k: data.get(k, "") for k in "ABCD"},
                        "answer": data.get("answer", "A"),
                        "doc_id": chunk.doc_id,
                        "chunk_id": chunk.chunk_id,
                        "label": "call_document",
                    })
                    count += 1
            except Exception:
                pass

        time.sleep(config.GEMINI_SLEEP)
        if count % 50 == 0:
            logger.info("doc_mcq_progress", extra={"generated": count})

    save_jsonl(out_path, results)
    logger.info("doc_mcq_done", extra={"total": len(results), "path": str(out_path)})
    print(f"[04] saved {len(results)} MCQ → {out_path}")


def gen_api_qa(n_per_api: int = 2) -> None:
    """Gen câu hỏi tự nhiên từ API schemas."""
    config.ensure_dirs()
    out_path = config.SYNTHETIC_DIR / "api_qa.jsonl"

    if not config.API_SCHEMAS.exists():
        raise FileNotFoundError(f"schemas.json not found: {config.API_SCHEMAS}")

    schemas = json.loads(config.API_SCHEMAS.read_text(encoding="utf-8"))
    model = _gemini_client()
    results = []

    for func_code, entry in schemas.items():
        prompt = f"""Dưới đây là một API trong hệ thống quản lý dự án Viettel.

func_code: {func_code}
Tên: {entry['name']}
Mô tả: {entry['description']}
Ví dụ câu hỏi: {entry['example_question']}

Hãy tạo {n_per_api} câu hỏi tự nhiên tiếng Việt khác nhau mà người dùng có thể hỏi để trigger API này.
Mỗi câu hỏi trên 1 dòng, không đánh số."""

        raw = _call_gemini(model, prompt)
        if raw:
            lines = [l.strip() for l in raw.strip().split("\n") if l.strip() and len(l.strip()) > 10]
            for q in lines[:n_per_api]:
                results.append({"question": q, "func_code": func_code, "label": "call_api"})

        time.sleep(config.GEMINI_SLEEP)

    save_jsonl(out_path, results)
    logger.info("api_qa_done", extra={"total": len(results), "path": str(out_path)})
    print(f"[04] saved {len(results)} API Q&A → {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["doc", "api", "all"], default="all")
    args = parser.parse_args()

    if args.mode in {"doc", "all"}:
        gen_doc_mcq()
    if args.mode in {"api", "all"}:
        gen_api_qa()
