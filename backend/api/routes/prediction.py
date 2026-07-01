from fastapi import APIRouter

router = APIRouter(prefix="/prediction", tags=["Prediction"])


@router.get("/")
def test():
    return {"message": "Prediction API Working"}
