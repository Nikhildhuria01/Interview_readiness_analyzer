import random
import pandas as pd

NUM_SAMPLES = 1000

data = []

for _ in range(NUM_SAMPLES):

    fluency = round(random.uniform(40, 100), 2)

    correctness = round(random.uniform(30, 100), 2)

    eye_contact = round(random.uniform(40, 100), 2)

    posture = round(random.uniform(35, 100), 2)

    head_stability = round(random.uniform(45, 100), 2)

    readiness = (
        0.25 * fluency
        + 0.35 * correctness
        + 0.15 * eye_contact
        + 0.15 * posture
        + 0.10 * head_stability
    )

    readiness += random.uniform(-5, 5)

    readiness = max(0, min(100, readiness))

    data.append(
        [
            fluency,
            correctness,
            eye_contact,
            posture,
            head_stability,
            round(readiness, 2),
        ]
    )

df = pd.DataFrame(
    data,
    columns=[
        "fluency",
        "correctness",
        "eye_contact",
        "posture",
        "head_stability",
        "readiness",
    ],
)

df.to_csv("backend/ml/interview_training_dataset.csv", index=False)

print(df.head())

print("\nDataset Generated Successfully!")

print(f"Total Samples : {len(df)}")
