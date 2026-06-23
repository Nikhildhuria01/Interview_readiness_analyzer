def calculate_overall_score(

    fluency_score,

    correctness_score,

    eye_contact_score,

    posture_score,

    head_stability_score

):

    overall_score = (

        fluency_score * 0.25

        +

        correctness_score * 0.40

        +

        eye_contact_score * 0.15

        +

        posture_score * 0.10

        +

        head_stability_score * 0.10

    )

    return round(
        overall_score,
        2
    )