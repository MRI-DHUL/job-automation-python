from fastapi import FastAPI, Depends
from app.jobs.routes import router as jobs_router
from app.auth.routes import router as auth_router
from app.auth.deps import get_current_user
from db.models import User

app = FastAPI(title="Job Automation API")

app.include_router(jobs_router)
app.include_router(auth_router)

@app.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role,
    }