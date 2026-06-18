import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1000

data = []

for _ in range(rows):

    correctness = np.random.randint(40, 101)
    eye_contact = np.random.randint(30, 101)
    posture = np.random.randint(30, 101)
    fluency = np.random.randint(30, 101)

    speech_rate = np.random.randint(80, 181)

    pause_count = np.random.randint(0, 21)
    filler_count = np.random.randint(0, 16)

    smile_score = np.random.randint(10, 101)
    head_stability = np.random.randint(20, 101)

    speech_rate_score = min(100, max(0, 100 - abs(130 - speech_rate)))

    confidence = (
        0.25 * correctness
        + 0.15 * eye_contact
        + 0.10 * posture
        + 0.15 * fluency
        + 0.10 * smile_score
        + 0.10 * head_stability
        + 0.10 * speech_rate_score
        - 0.03 * pause_count
        - 0.02 * filler_count
    )

    confidence = round(max(0, min(100, confidence)), 2)

    data.append(
        [
            correctness,
            eye_contact,
            posture,
            fluency,
            speech_rate,
            pause_count,
            filler_count,
            smile_score,
            head_stability,
            confidence,
        ]
    )

columns = [
    "correctness",
    "eye_contact",
    "posture",
    "fluency",
    "speech_rate",
    "pause_count",
    "filler_count",
    "smile_score",
    "head_stability",
    "confidence_label",
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("data/raw/interview_dataset.csv", index=False)

print("Dataset generated successfully!")
