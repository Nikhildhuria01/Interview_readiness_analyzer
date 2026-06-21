import json


def save_features(eye_contact, posture, stability, fluency, correctness):

    data = {
        "eye_contact": eye_contact,
        "posture": posture,
        "stability": stability,
        "fluency": fluency,
        "correctness": correctness,
    }

    with open("backend/interview/interview_features.json", "w") as f:

        json.dump(data, f, indent=4)

    print("\nFeatures Saved Successfully!")
