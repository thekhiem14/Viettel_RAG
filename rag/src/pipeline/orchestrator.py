from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from intent.src.classifier import predict
from rag.src.pipeline import api_pipeline, doc_pipeline
from shared.types import Question
from shared.utils.logger import get_logger

import config

logger = get_logger("orchestrator", config.LOGS_DIR)


def run_one(question: Question) -> dict:
    """Route 1 câu hỏi → đúng pipeline → output dict."""
    label, confidence = predict(question)
    logger.info("intent", extra={"id": question.id, "label": label, "confidence": confidence})

    try:
        if label == "call_document":
            return doc_pipeline.run(question)
        else:
            return api_pipeline.run(question)
    except Exception as e:
        logger.error("pipeline_error", extra={"id": question.id, "error": str(e)})
        return {
            "id": question.id,
            "function_code": label,
            "function_result": "",
            "time_response": 0.0,
        }


def run_batch(questions: list[Question]) -> list[dict]:
    """Chạy tuần tự, log từng câu. Dùng cho eval + inference."""
    results = []
    for i, q in enumerate(questions):
        result = run_one(q)
        results.append(result)
        if (i + 1) % 10 == 0:
            logger.info("batch_progress", extra={"done": i + 1, "total": len(questions)})
    return results
