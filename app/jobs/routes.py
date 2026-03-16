from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.automation.pipeline import run_job_pipeline
from db.database import SessionLocal
from db.models import Job
from app.auth.deps import get_current_user
from db.models import User

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/fetch")
def fetch_jobs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = run_job_pipeline(db)

    return {
        "message": "Jobs fetched successfully",
        "details": result
    }

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def list_jobs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    jobs = db.query(Job).order_by(Job.created_at.desc()).limit(50).all()

    return jobs