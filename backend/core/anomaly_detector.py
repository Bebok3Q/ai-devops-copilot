import re
from collections import Counter
from sklearn.ensemble import IsolationForest
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import os
import joblib


MODEL_DIR = "core/model"
os.makedirs(MODEL_DIR, exist_ok=True)

VEC_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")
MODEL_PATH = os.path.join(MODEL_DIR, "anomaly_model.pkl")

def train_anomaly_model(logs: list[str]):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(logs)
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X.toarray())

    joblib.dump(vectorizer, VEC_PATH)
    joblib.dump(model, MODEL_PATH)

    return {"status": "Model trained", "samples": len(logs)}

def detect_anomalies(log_text: str):
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VEC_PATH):
        return {"is_anomalous": False, "details": "Model not trained yet."}

    vectorizer = joblib.load(VEC_PATH)
    model = joblib.load(MODEL_PATH)

    X = vectorizer.transform([log_text])
    prediction = model.predict(X.toarray())[0]  # -1 = anomaly, 1 = normal
    return {
        "is_anomalous": prediction == -1,
        "details": "Detected via ML-based Isolation Forest"
    }



