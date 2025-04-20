from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class LogInput(BaseModel):
    content: str

class LogAnalysisResult(BaseModel):
    error_message: str
    likely_cause: Optional[str]
    suggested_fix: Optional[str]

class AnomalyResult(BaseModel):
    is_anomalous: bool
    details: Optional[str]

class DashboardLog(BaseModel):
    id: int
    timestamp: datetime
    error: str
    is_anomalous: bool
    patch: Optional[str]