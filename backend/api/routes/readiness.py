from fastapi import APIRouter
from pydantic import BaseModel

from ml.predict_readiness import (
    predict_readiness,
    get_readiness_status,
)

from ml.save_training_data import (
    save_training_data,
)

router = APIRouter(
    prefix="/readiness",
    tags=["Readiness"],
)


class ReadinessRequest(BaseModel):

    fluency: float

    correctness: float

    eye_contact: float

    posture: float

    head_stability: float


@router.post("/predict")
def predict(request: ReadinessRequest):

    score = predict_readiness(

        request.fluency,

        request.correctness,

        request.eye_contact,

        request.posture,

        request.head_stability,

    )

    status = get_readiness_status(score)

    save_training_data(

        request.fluency,

        request.correctness,

        request.eye_contact,

        request.posture,

        request.head_stability,

        score,

    )

    return {

        "readiness_score": score,

        "readiness_status": status,

    }