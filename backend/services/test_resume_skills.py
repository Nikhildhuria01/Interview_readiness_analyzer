from pathlib import Path

from pdf_parser import extract_text_from_pdf
from resume_parser import extract_resume_skills

BASE_DIR = Path(__file__).resolve().parents[2]

pdf_path = (
    BASE_DIR /
    "data/resumes/testresume.pdf"
)

resume_text = extract_text_from_pdf(
    pdf_path
)

skills = extract_resume_skills(
    resume_text
)

print("\nDetected Skills:\n")

print(skills)