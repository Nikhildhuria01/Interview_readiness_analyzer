from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

software = pd.read_csv(
    BASE_DIR / "data/raw/Software_Questions.csv",
    encoding="latin1"
)

full = pd.read_csv(
    BASE_DIR / "data/raw/full_interview_questions_dataset.csv",
    encoding="latin1"
)

print("\n=== SOFTWARE QUESTIONS ===")
print(software.columns)

print("\nFirst 5 rows:")
print(software.head())

print("\n=== FULL QUESTIONS ===")
print(full.columns)

print("\nFirst 5 rows:")
print(full.head())