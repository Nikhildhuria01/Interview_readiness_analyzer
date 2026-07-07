import json


def save_emotion_features(

    emotion,

    confidence_score,

    engagement_score,

    nervousness_score

):

    data = {

        "emotion": emotion,

        "confidence_score":
            confidence_score,

        "engagement_score":
            engagement_score,

        "nervousness_score":
            nervousness_score
    }

    with open(

        "interview/emotion_features.json",

        "w"

    ) as f:

        json.dump(

            data,

            f,

            indent=4
        )

    print(
        "Emotion features saved."
    )