from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.resume_parser import extract_resume_skills
from backend.services.job_parser import extract_job_skills
from backend.interview.question_engine import generate_interview_questions

router = APIRouter(prefix="/questions", tags=["Questions"])


class QuestionRequest(BaseModel):
    resume_text: str
    job_text: str


@router.post("/generate")
def generate_questions(request: QuestionRequest):

    resume_skills = extract_resume_skills(request.resume_text)

    job_skills = extract_job_skills(request.job_text)

    questions = generate_interview_questions(resume_skills, job_skills)

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "total_questions": len(questions),
        "questions": questions,
    }
