import json


def load_features():

    with open(
        "backend/interview/interview_features.json",
        "r"
    ) as f:

        return json.load(f)