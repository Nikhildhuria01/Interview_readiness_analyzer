from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

questions_df = pd.read_csv(
    BASE_DIR /
    "data/raw/full_interview_questions_dataset.csv",
    encoding="latin1"
)

def get_questions(
    role,
    n=10
):

    role_questions = questions_df[
        questions_df["role"]
        .str.lower()
        ==
        role.lower()
    ]

    return (
        role_questions["question"]
        .head(n)
        .tolist()
    )
