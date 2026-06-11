from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

datasets = [
    "Software_Questions.csv",
    "full_interview_questions_dataset.csv",
    "job_title_des.csv",
    "Resume.csv",
]

for file in datasets:

    path = BASE_DIR / "data" / "raw" / file

    try:
        df = pd.read_csv(path, encoding="latin1")

        # Basic cleaning
        df.drop_duplicates(inplace=True)
        df.dropna(how="all", inplace=True)

        output_name = file.replace(".csv", "_clean.csv")

        output_path = BASE_DIR / "data" / "processed" / output_name

        df.to_csv(output_path, index=False)

        print(f"Saved: {output_name}")

    except Exception as e:
        print(f"Error in {file}: {e}")
