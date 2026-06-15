from pathlib import Path

from pdf_parser import extract_text_from_pdf
from resume_parser import extract_resume_skills
from job_parser import extract_job_skills
from skill_gap import compare_skills
from readiness_score import calculate_score

from question_recommender import (
    get_role_questions,
    get_existing_skill_questions,
    get_missing_skill_questions,
)

from report_generator import generate_report

BASE_DIR = Path(__file__).resolve().parents[2]

# ==========================================
# LOAD RESUME PDF
# ==========================================

pdf_path = BASE_DIR / "data/resumes/rss.pdf"

resume_text = extract_text_from_pdf(pdf_path)

# ==========================================
# TEST JOB DESCRIPTION
# ==========================================

job_description = """
Software Engineer

Required Skills:

Python
Git
Linux
Docker
Jenkins
"""

# ==========================================
# SKILL EXTRACTION
# ==========================================

resume_skills = extract_resume_skills(resume_text)

job_skills = extract_job_skills(job_description)

# ==========================================
# SKILL GAP ANALYSIS
# ==========================================

matched, missing = compare_skills(resume_skills, job_skills)

# ==========================================
# READINESS SCORE
# ==========================================

score = calculate_score(matched, job_skills)

# ==========================================
# QUESTIONS
# ==========================================

role_questions = get_role_questions("Software Engineer")

existing_questions = get_existing_skill_questions(matched)

missing_questions = get_missing_skill_questions(missing)

# ==========================================
# OUTPUT
# ==========================================

print("\n" + "=" * 60)
print("INTERVIEW READINESS REPORT")
print("=" * 60)

print("\nResume Skills:")
print(resume_skills)

print("\nJob Skills:")
print(job_skills)

print("\nMatched Skills:")
print(matched)

print("\nMissing Skills:")
print(missing)

print(f"\nReadiness Score: {score:.2f}%")

print("\nROLE QUESTIONS")
for q in role_questions[:5]:
    print("-", q)

print("\nMATCHED SKILL QUESTIONS")
for q in existing_questions[:10]:
    print("-", q)

print("\nMISSING SKILL QUESTIONS")
for q in missing_questions[:10]:
    print("-", q)

# ==========================================
# PDF REPORT
# ==========================================

generate_report(
    role="Software Engineer",
    readiness_score=score,
    resume_skills=resume_skills,
    matched=matched,
    missing=missing,
    role_questions=role_questions,
    missing_questions=missing_questions,
)

print("\nPDF REPORT GENERATED")
print("=" * 60)
