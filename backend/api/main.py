from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes.resume import router as resume_router
from backend.api.routes.interview import router as interview_router
from backend.api.routes.report import router as report_router
from backend.api.routes.prediction import router as prediction_router
from backend.api.routes.job import router as job_router
from backend.api.routes.analysis import router as analysis_router
from backend.api.routes.questions import router as questions_router

app = FastAPI(title="AI Interview Readiness Analyzer", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later we'll restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume_router)
app.include_router(interview_router)
app.include_router(report_router)
app.include_router(prediction_router)
app.include_router(job_router)
app.include_router(analysis_router)
app.include_router(questions_router)


@app.get("/")
def home():
    return {"status": "Backend Running", "version": "1.0"}
