from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.resume import router as resume_router
from api.routes.interview import router as interview_router
from api.routes.report import router as report_router
from api.routes.prediction import router as prediction_router
from api.routes.job import router as job_router
from api.routes.analysis import router as analysis_router
from api.routes.questions import router as questions_router
from api.routes.camera import router as camera_router
from api.routes.readiness import router as readiness_router

app = FastAPI(title="AI Interview Readiness Analyzer", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Resume
app.include_router(resume_router, prefix="/resume", tags=["Resume"])

# Interview
app.include_router(interview_router, prefix="/interview", tags=["Interview"])

# Report
app.include_router(report_router, prefix="/report", tags=["Report"])

# Prediction
app.include_router(prediction_router, prefix="/prediction", tags=["Prediction"])

# Job Description
app.include_router(job_router, prefix="/job", tags=["Job Description"])

# Analysis
app.include_router(analysis_router, prefix="/analysis", tags=["Analysis"])

# Questions
app.include_router(questions_router, prefix="/questions", tags=["Questions"])

app.include_router(camera_router, prefix="/camera", tags=["Camera"])
app.include_router(readiness_router)


@app.get("/")
def home():
    return {"status": "Backend Running", "version": "1.0"}
