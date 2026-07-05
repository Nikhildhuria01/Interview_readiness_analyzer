from fastapi import APIRouter

router = APIRouter()


@router.post("/analyze-frame")
def analyze_frame():

    return {
        "message": "Camera API Working"
    }