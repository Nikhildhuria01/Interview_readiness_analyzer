from fastapi import APIRouter
from fastapi.responses import FileResponse
from pydantic import BaseModel

from services.interview_report_generator import (
    generate_interview_report,
)

router = APIRouter(
    prefix="/report",
    tags=["Report"],
)


@router.get("/")
def test():
    return {"message": "Report API Working"}


class ReportRequest(BaseModel):

    readiness_score: float

    readiness_status: str

    eye_contact: float

    posture: float

    head_stability: float

    question_results: list


@router.post("/generate")
def generate_report(request: ReportRequest):

    pdf_path = generate_interview_report(

        readiness_score=request.readiness_score,

        readiness_status=request.readiness_status,

        eye_contact=request.eye_contact,

        posture=request.posture,

        head_stability=request.head_stability,

        question_results=request.question_results,

    )

    return FileResponse(

        pdf_path,

        media_type="application/pdf",

        filename="Interview_Report.pdf",

    )
