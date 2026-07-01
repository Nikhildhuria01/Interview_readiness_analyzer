from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.resume_parser import extract_resume_skills
from backend.services.job_parser import extract_job_skills
from backend.services.skill_gap import compare_skills

router = APIRouter(prefix="/analysis", tags=["Analysis"])


class AnalysisRequest(BaseModel):

    resume_text: str

    job_text: str


@router.post("/skill-gap")
def skill_gap(request: AnalysisRequest):

    resume_skills = extract_resume_skills(request.resume_text)

    job_skills = extract_job_skills(request.job_text)

    matched, missing = compare_skills(resume_skills, job_skills)

    if len(job_skills) == 0:

        readiness = 0

    else:

        readiness = round(len(matched) / len(job_skills) * 100, 2)

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched,
        "missing_skills": missing,
        "readiness_percentage": readiness,
    }
