from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="user")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_login = Column(DateTime(timezone=True))


class UserProfile(Base):
    __tablename__ = "user_profiles"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    headline = Column(String(200))
    skills = Column(Text)
    experience_years = Column(Integer)
    preferred_location = Column(String(200))
    preferred_roles = Column(Text)
    resume_url = Column(String(500))
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    company = Column(String(200))
    location = Column(String(200))
    employment_type = Column(String(50))
    source = Column(String(100))
    external_id = Column(String(100))
    url = Column(String(500), unique=True)
    description = Column(Text)
    salary_min = Column(Integer)
    salary_max = Column(Integer)
    currency = Column(String(10))
    posted_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class JobSkill(Base):
    __tablename__ = "job_skills"
    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    skill_name = Column(String(100), nullable=False)


class SavedJob(Base):
    __tablename__ = "saved_jobs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    saved_at = Column(DateTime(timezone=True), server_default=func.now())


class AppliedJob(Base):
    __tablename__ = "applied_jobs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    status = Column(String(50))
    applied_at = Column(DateTime(timezone=True), server_default=func.now())
    notes = Column(Text)


class SearchHistory(Base):
    __tablename__ = "search_history"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    keywords = Column(String(200))
    location = Column(String(200))
    filters_json = Column(Text)
    searched_at = Column(DateTime(timezone=True), server_default=func.now())


class JobAlert(Base):
    __tablename__ = "job_alerts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    keywords = Column(String(200))
    location = Column(String(200))
    frequency = Column(String(50))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(200))
    message = Column(Text)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class FetchLog(Base):
    __tablename__ = "fetch_logs"
    id = Column(Integer, primary_key=True)
    source = Column(String(100))
    jobs_fetched = Column(Integer)
    status = Column(String(50))
    error_message = Column(Text)
    fetched_at = Column(DateTime(timezone=True), server_default=func.now())