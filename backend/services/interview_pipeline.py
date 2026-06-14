from pathlib import Path
import pandas as pd

from resume_parser import extract_resume_skills
from job_parser import extract_job_skills
from skill_gap import compare_skills

from question_recommender import (
    get_role_questions,
    get_existing_skill_questions,
    get_missing_skill_questions,
)

from readiness_score import calculate_score

BASE_DIR = Path(__file__).resolve().parents[2]

# ==========================================
# LOAD DATASETS
# ==========================================

resumes = pd.read_csv(BASE_DIR / "data/processed/tech_resumes.csv")

jobs = pd.read_csv(BASE_DIR / "data/processed/tech_jobs.csv")

# ==========================================
# SELECT RESUME
# ==========================================

from pdf_parser import extract_text_from_pdf

pdf_path = (
    BASE_DIR /
    "data/resumes/testresume.pdf"
)

resume_text = extract_text_from_pdf(
    pdf_path
)

# ==========================================
# SELECT JOB ROLE
# ==========================================

target_role = "Software Engineer"

job_text = jobs[jobs["Job Title"] == target_role].iloc[0]["Job Description"]

# ==========================================
# EXTRACT SKILLS
# ==========================================

resume_skills = extract_resume_skills(resume_text)

job_skills = extract_job_skills(job_text)

# ==========================================
# SKILL GAP ANALYSIS
# ==========================================

matched, missing = compare_skills(resume_skills, job_skills)

# ==========================================
# READINESS SCORE
# ==========================================

score = calculate_score(matched, job_skills)

# ==========================================
# QUESTION GENERATION
# ==========================================

role_questions = get_role_questions(target_role, n=5)

existing_skill_questions = get_existing_skill_questions(resume_skills)

missing_skill_questions = get_missing_skill_questions(missing)

# ==========================================
# FINAL REPORT
# ==========================================

print("\n")
print("=" * 50)
print("INTERVIEW READINESS REPORT")
print("=" * 50)

print("\nTarget Role:")
print(target_role)

print("\nReadiness Score:")
print(score, "%")

print("\nResume Skills:")
print(resume_skills)

print("\nJob Skills:")
print(job_skills)

print("\nMatched Skills:")
print(matched)

print("\nMissing Skills:")
print(missing)

print("\n")
print("=" * 50)
print("ROLE BASED QUESTIONS")
print("=" * 50)

for q in role_questions:
    print("-", q)

print("\n")
print("=" * 50)
print("EXISTING SKILL QUESTIONS")
print("=" * 50)

for q in existing_skill_questions:
    print("-", q)

print("\n")
print("=" * 50)
print("MISSING SKILL QUESTIONS")
print("=" * 50)

for q in missing_skill_questions:
    print("-", q)
