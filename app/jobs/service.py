from sqlalchemy.orm import Session
from db.models import Job


def save_jobs(db: Session, jobs: list):
    saved_jobs = []

    for job in jobs:

        # Avoid duplicates using URL
        existing = db.query(Job).filter(Job.url == job["url"]).first()
        if existing:
            continue

        new_job = Job(
            title=job.get("title"),
            company=job.get("company"),
            location=job.get("location"),
            source=job.get("source"),
            url=job.get("url"),
            description=job.get("description"),
        )

        db.add(new_job)
        saved_jobs.append(new_job)

    db.commit()

    return saved_jobs