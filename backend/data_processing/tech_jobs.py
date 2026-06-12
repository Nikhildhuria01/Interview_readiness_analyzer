from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

jobs = pd.read_csv(
    BASE_DIR / "data/processed/job_title_des_clean.csv"
)

TECH_ROLES = [
    "Software Engineer",
    "DevOps Engineer",
    "Machine Learning",
    "Java Developer",
    "Django Developer",
    "Full Stack Developer",
    "JavaScript Developer",
    "Database Administrator"
]

tech_jobs = jobs[
    jobs["Job Title"].isin(TECH_ROLES)
]

print("Original Jobs:", jobs.shape)
print("Tech Jobs:", tech_jobs.shape)

tech_jobs.to_csv(
    BASE_DIR / "data/processed/tech_jobs.csv",
    index=False
)
print(tech_jobs["Job Title"].value_counts())