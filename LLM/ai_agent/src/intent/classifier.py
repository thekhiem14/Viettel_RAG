"""
Intent Classifier — phân loại câu hỏi thành 'call_document' hoặc 'call_api'.

Hiện tại: stub luôn trả về 'call_document' vì chưa có labeled data cho call_api.
Sau khi có data: train TF-IDF + Logistic Regression hoặc embedding centroid,
load model từ models/intent_classifier.pkl.
"""
import os
import pickle
from typing import Literal

IntentType = Literal['call_document', 'call_api']

_DEFAULT_INTENT: IntentType = 'call_document'


class IntentClassifier:
    def __init__(self, model_path: str | None = None):
        self.model = None
        if model_path and os.path.exists(model_path):
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)
            print(f"IntentClassifier loaded từ {model_path}")
        else:
            print("IntentClassifier: chưa có model, dùng default 'call_document'")

    def predict(self, question: str) -> IntentType:
        if self.model is None:
            return _DEFAULT_INTENT
        result = self.model.predict([question])[0]
        return result
