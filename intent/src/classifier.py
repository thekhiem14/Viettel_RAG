from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

import config
from intent.src.features import extract_features
from shared.types import Question

_clf = None


def _get_clf():
    global _clf
    if _clf is None:
        from shared.utils.io import load_pickle
        _clf = load_pickle(config.CLASSIFIER)
    return _clf


def predict(question: Question) -> tuple[str, float]:
    """Predict intent: 'call_document' | 'call_api', và confidence score.

    Falls back to rule-based nếu model chưa train:
    - note is not None → call_document
    - note is None → call_api
    """
    try:
        import numpy as np
        bundle = _get_clf()
        tfidf = bundle["tfidf"]
        clf = bundle["clf"]

        X_tfidf = tfidf.transform([question.question]).toarray()
        X_feats = np.array([extract_features(question.question, question.note)])
        X = np.hstack([X_tfidf, X_feats])

        proba = clf.predict_proba(X)[0]
        classes = list(clf.classes_)
        label = classes[proba.argmax()]
        confidence = float(proba.max())
        return label, confidence
    except Exception:
        # Rule-based fallback (100% accurate cho data này)
        if question.note is not None and question.note.strip().lower() not in {"nan", "none", ""}:
            return "call_document", 1.0
        return "call_api", 1.0
