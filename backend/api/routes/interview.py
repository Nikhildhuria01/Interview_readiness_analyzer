from fastapi import APIRouter

router = APIRouter(prefix="/interview", tags=["Interview"])


@router.get("/")
def test():
    return {"message": "Interview API Working"}
