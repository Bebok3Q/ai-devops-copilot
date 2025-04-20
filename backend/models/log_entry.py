from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .database import Base

class LogEntry(Base):
    __tablename__ = "log_entries"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    error_message = Column(String(512))
    is_anomalous = Column(Integer)  # 0 or 1
    patch = Column(String(512), nullable=True) # Ustawione jako nullable=True
    created_at = Column(DateTime, default=datetime.utcnow)