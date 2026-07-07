import random
import pandas as pd

data = []

for _ in range(1000):

    fluency = random.randint(40, 100)

    correctness = random.randint(40, 100)

    eye_contact = random.randint(40, 100)

    posture = random.randint(40, 100)

    head_stability = random.randint(40, 100)

    readiness_score = round(
        fluency * 0.20
        + correctness * 0.35
        + eye_contact * 0.15
        + posture * 0.15
        + head_stability * 0.15,
        2,
    )

    data.append(
        [fluency, correctness, eye_contact, posture, head_stability, readiness_score]
    )

df = pd.DataFrame(
    data,
    columns=[
        "fluency",
        "correctness",
        "eye_contact",
        "posture",
        "head_stability",
        "readiness_score",
    ],
)

df.to_csv("ml/interview_dataset.csv", index=False)

print("Dataset Generated Successfully!")
print(df.head())
