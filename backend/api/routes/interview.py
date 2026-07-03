from pathlib import Path
import shutil
import uuid

from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from backend.interview.interview_service import analyze_answer

router = APIRouter()

# Temporary folder for uploaded audio
TEMP_DIR = Path("backend/interview/temp")
TEMP_DIR.mkdir(parents=True, exist_ok=True)


@router.get("/")
def test():
    return {"message": "Interview API Working"}


@router.post("/analyze")
async def analyze_interview(question: str = Form(...), audio: UploadFile = File(...)):
    try:

        audio_filename = f"{uuid.uuid4()}.wav"

        audio_path = TEMP_DIR / audio_filename

        transcript_path = TEMP_DIR / f"{audio_path.stem}.txt"

        with open(audio_path, "wb") as buffer:
            shutil.copyfileobj(audio.file, buffer)

        result = analyze_answer(
            question=question,
            audio_file=str(audio_path),
            transcript_file=str(transcript_path),
            answer_duration=30,
        )

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
