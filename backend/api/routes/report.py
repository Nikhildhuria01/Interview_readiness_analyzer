from fastapi import APIRouter

router = APIRouter(prefix="/report", tags=["Report"])


@router.get("/")
def test():
    return {"message": "Report API Working"}
