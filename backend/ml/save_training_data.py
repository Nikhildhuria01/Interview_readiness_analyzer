import os
import pandas as pd


def save_training_data(

    fluency,

    correctness,

    eye_contact,

    posture,

    head_stability,

    readiness_score

):

    dataset_path = "backend/ml/real_interview_dataset.csv"

    new_data = pd.DataFrame([{

        "fluency": float(fluency),

        "correctness": float(correctness),

        "eye_contact": float(eye_contact),

        "posture": float(posture),

        "head_stability": float(head_stability),

        "readiness": float(readiness_score)

    }])

    if os.path.exists(dataset_path):

        old_data = pd.read_csv(dataset_path)

        new_data = pd.concat(

            [old_data, new_data],

            ignore_index=True

        )

    new_data.to_csv(

        dataset_path,

        index=False

    )

    print("Training dataset updated successfully!")