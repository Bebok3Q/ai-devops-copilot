from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.schemas import LogInput, LogAnalysisResult, DashboardLog
from core.analyzer import analyze_log
from core.patch_generator import suggest_fix
from models.database import SessionLocal, get_db
from models.log_entry import LogEntry

router = APIRouter()

@router.post("/analyze", response_model=LogAnalysisResult)
def analyze_and_store(log_input: LogInput, db: Session = Depends(get_db)):
    result = analyze_log(log_input.content)
    patch_data = suggest_fix(result["error_message"])
    suggested_fix_value = patch_data["suggested_patch"] if patch_data else None

    db_log = LogEntry(
        content=log_input.content,
        error_message=result["error_message"],
        is_anomalous=int(result["is_anomalous"]),
        patch=suggested_fix_value  # Zapisujemy sugerowaną poprawkę
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    db.close()

    return {
        "error_message": result["error_message"],
        "is_anomalous": result["is_anomalous"],
        "suggested_fix": suggested_fix_value,
        "likely_cause": result.get("likely_cause"),
    }

@router.post("/suggest-patch")
def suggest_patch_endpoint(log_input: LogInput):
    result = analyze_log(log_input.content)
    suggestion = suggest_fix(result["error_message"])

    if suggestion:
        return suggestion
    else:
        raise HTTPException(status_code=404, detail="No patch suggestion found for this error.")



@router.get("/dashboard", response_model=list[DashboardLog])
def get_dashboard(db: Session = Depends(get_db)):
    logs = db.query(LogEntry).order_by(LogEntry.created_at.desc()).limit(20).all()
    db.close()

    return [
        {
            "id": log.id,
            "timestamp": log.created_at,
            "error": log.error_message,
            "is_anomalous": bool(log.is_anomalous),
            "patch": log.patch,
        }
        for log in logs
    ]

