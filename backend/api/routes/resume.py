from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import tempfile
import os

from services.resume_parser import extract_resume_skills
from services.pdf_parser import extract_text_from_pdf

router = APIRouter(prefix="/resume", tags=["Resume"])


class ResumeRequest(BaseModel):
    resume_text: str


# ==========================================
# Extract Skills from Resume Text
# ==========================================


@router.post("/extract")
def extract_skills(request: ResumeRequest):

    skills = extract_resume_skills(request.resume_text)

    return {"skills": skills, "total_skills": len(skills)}


# ==========================================
# Upload Resume PDF
# ==========================================


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:

        temp.write(await file.read())

        temp_path = temp.name

    try:

        resume_text = extract_text_from_pdf(temp_path)

        skills = extract_resume_skills(resume_text)

        return {
            "resume_text": resume_text,
            "skills": skills,
            "total_skills": len(skills),
        }

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)
