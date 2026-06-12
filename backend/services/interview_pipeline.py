from pathlib import Path
import pandas as pd

from resume_parser import extract_resume_skills
from job_parser import extract_job_skills
from skill_gap import compare_skills
from question_generator import generate_questions

BASE_DIR = Path(__file__).resolve().parents[2]

resumes = pd.read_csv(
    BASE_DIR / "data/processed/tech_resumes.csv"
)

jobs = pd.read_csv(
    BASE_DIR / "data/processed/tech_jobs.csv"
)

resume_text = resumes.iloc[0]["Resume_str"]

job_text = jobs[
    jobs["Job Title"] == "DevOps Engineer"
].iloc[0]["Job Description"]

resume_skills = extract_resume_skills(
    resume_text
)

job_skills = extract_job_skills(
    job_text
)

matched, missing = compare_skills(
    resume_skills,
    job_skills
)
questions = generate_questions(
    missing
)

print("\nRecommended Questions:")

for q in questions:
    print("-", q)
print("\nResume Skills:")
print(resume_skills)

print("\nJob Skills:")
print(job_skills)

print("\nMatched Skills:")
print(matched)

print("\nMissing Skills:")
print(missing)