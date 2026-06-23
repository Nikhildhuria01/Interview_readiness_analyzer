import json


def save_results(results):

    with open(
        "backend/interview/interview_results.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            results,
            f,
            indent=4
        )

    print(
        "\nResults Saved Successfully!"
    )