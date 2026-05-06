"""Train intent classifier: TF-IDF + LogisticRegression + feature engineering.

Data sources:
  1. data/example_data.xlsx   — 100 real examples (50 call_doc + 50 call_api)
  2. synthetic/doc_qa.jsonl   — ~500 generated MCQ (call_document)
  3. synthetic/api_qa.jsonl   — ~300 generated Q&A (call_api)

Output: artifacts/classifier/intent.pkl

Usage:
    python rag/scripts/05_train_classifier.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import config
from intent.src.features import extract_features
from shared.utils.io import load_jsonl, save_pickle
from shared.utils.logger import get_logger

logger = get_logger("05_train_classifier", config.LOGS_DIR)


def _load_training_data() -> tuple[list, list]:
    """Load tất cả training data, trả về (X, y)."""
    import pandas as pd
    from sklearn.pipeline import Pipeline, FeatureUnion
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.preprocessing import FunctionTransformer

    texts, labels = [], []

    # 1. Real examples from Excel
    excel_path = config.DATA_DIR / "example_data.xlsx"
    if excel_path.exists():
        df = pd.read_excel(excel_path)
        for _, row in df.iterrows():
            note = None if str(row.get("note", "")).lower() in {"nan", "none", ""} else str(row["note"])
            label = "call_document" if note else "call_api"
            texts.append((str(row["fun_question"]), note))
            labels.append(label)
        logger.info("loaded_excel", extra={"count": len(df)})

    # 2. Synthetic doc MCQ
    doc_qa_path = config.SYNTHETIC_DIR / "doc_qa.jsonl"
    if doc_qa_path.exists():
        for rec in load_jsonl(doc_qa_path):
            note_text = "A, x\n B, x\n C, x\n D, x"
            texts.append((rec["question"], note_text))
            labels.append("call_document")
        logger.info("loaded_doc_qa", extra={"count": sum(1 for l in labels if l == "call_document")})

    # 3. Synthetic API Q&A
    api_qa_path = config.SYNTHETIC_DIR / "api_qa.jsonl"
    if api_qa_path.exists():
        for rec in load_jsonl(api_qa_path):
            texts.append((rec["question"], None))
            labels.append("call_api")
        logger.info("loaded_api_qa", extra={"count": sum(1 for l in labels if l == "call_api")})

    return texts, labels


def train() -> None:
    config.ensure_dirs()
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import Pipeline
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.preprocessing import FunctionTransformer
    from sklearn.pipeline import FeatureUnion
    import numpy as np

    texts, labels = _load_training_data()
    if not texts:
        raise RuntimeError("No training data found.")

    questions = [t[0] for t in texts]
    notes = [t[1] for t in texts]

    # TF-IDF trên question text
    tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2), sublinear_tf=True)
    X_tfidf = tfidf.fit_transform(questions).toarray()

    # Hand-crafted features
    X_feats = np.array([extract_features(q, n) for q, n in zip(questions, notes)])

    X = np.hstack([X_tfidf, X_feats])

    clf = LogisticRegression(max_iter=1000, C=1.0, class_weight="balanced")
    clf.fit(X, labels)

    # Eval trên train set (không có test set riêng vì dùng hết 100 real)
    train_acc = clf.score(X, labels)
    logger.info("train_done", extra={"train_acc": train_acc, "n_samples": len(labels)})
    print(f"[05] train accuracy: {train_acc:.3f} | samples: {len(labels)}")

    # Save pipeline: (tfidf, clf) tuple
    save_pickle(config.CLASSIFIER, {"tfidf": tfidf, "clf": clf})
    print(f"[05] saved classifier → {config.CLASSIFIER}")


if __name__ == "__main__":
    train()
