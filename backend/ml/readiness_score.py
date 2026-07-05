from typing import Dict


def calculate_readiness_score(features: Dict):

    score = (

        features["resume_score"] * 0.20 +

        features["fluency_score"] * 0.20 +

        features["correctness_score"] * 0.30 +

        features["eye_contact"] * 0.10 +

        features["posture"] * 0.10 +

        features["head_stability"] * 0.10

    )

    score = round(score, 2)

    if score >= 85:

        level = "Excellent"

    elif score >= 70:

        level = "Good"

    elif score >= 50:

        level = "Needs Improvement"

    else:

        level = "Poor"

    return {

        "overall_score": score,

        "readiness_level": level

    }