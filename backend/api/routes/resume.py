from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.resume_parser import extract_resume_skills

router = APIRouter(prefix="/resume", tags=["Resume"])


class ResumeRequest(BaseModel):
    resume_text: str


@router.post("/extract")
def extract_skills(request: ResumeRequest):

    skills = extract_resume_skills(request.resume_text)

    return {"skills": skills, "total_skills": len(skills)}
