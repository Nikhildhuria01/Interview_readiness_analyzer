from typing import Dict


def aggregate_features(

    resume_score: float,

    fluency_score: float,

    correctness_score: float,

    eye_contact: float,

    posture: float,

    head_stability: float,

) -> Dict:

    return {

        "resume_score": resume_score,

        "fluency_score": fluency_score,

        "correctness_score": correctness_score,

        "eye_contact": eye_contact,

        "posture": posture,

        "head_stability": head_stability,

    }