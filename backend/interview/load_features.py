import json


def load_features():

    with open(
        "interview/interview_features.json",
        "r"
    ) as f:

        return json.load(f)