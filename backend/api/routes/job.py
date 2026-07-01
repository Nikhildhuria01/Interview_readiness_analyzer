from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.job_parser import extract_job_skills

router = APIRouter(prefix="/job", tags=["Job Description"])


class JobRequest(BaseModel):
    job_text: str


@router.post("/extract")
def extract_job(request: JobRequest):

    skills = extract_job_skills(request.job_text)

    return {"skills": skills, "total_skills": len(skills)}
