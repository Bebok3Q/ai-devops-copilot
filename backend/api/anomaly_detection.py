from fastapi import APIRouter
from models.schemas import LogInput, AnomalyResult
from core.anomaly_detector import detect_anomalies, train_anomaly_model
import os

router = APIRouter()

@router.post("/detect", response_model=AnomalyResult)
def detect(log_input: LogInput):
    result = detect_anomalies(log_input.content)
    return result

@router.post("/train")
def train():
    log_dir = "logs/sample_logs"
    logs = []

    for filename in os.listdir(log_dir):
        if filename.endswith(".txt") and "normal" in filename:
            with open(os.path.join(log_dir, filename), "r") as f:
                logs.append(f.read())

    if not logs:
        return {"error": "No normal logs found for training."}

    return train_anomaly_model(logs)
