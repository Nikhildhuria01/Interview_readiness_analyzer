from feature_aggregator import (
    calculate_overall_score
)

score = calculate_overall_score(

    fluency_score=85,

    correctness_score=90,

    eye_contact_score=80,

    posture_score=88,

    head_stability_score=82,

    confidence_score=86

)

print(
    f"Overall Score: {score}"
)