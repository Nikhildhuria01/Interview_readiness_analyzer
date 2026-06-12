from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

jobs = pd.read_csv(
    BASE_DIR / "data/processed/job_title_des_clean.csv"
)

print("\nColumns:\n")
print(jobs.columns)

print("\nFirst Job:\n")
print(jobs.iloc[0])
print(jobs["Job Title"].head(20))