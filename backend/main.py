from fastapi import FastAPI
from api import log_analysis, anomaly_detection
from fastapi.middleware.cors import CORSMiddleware
from models.database import Base, engine
from models.log_entry import LogEntry

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI DevOps Copilot API")

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(log_analysis.router, prefix="/log", tags=["Log Analysis"])
app.include_router(anomaly_detection.router, prefix="/anomaly", tags=["Anomaly Detection"])

@app.get("/")
def read_root():
    return {"message": "AI DevOps Copilot is running!"}
