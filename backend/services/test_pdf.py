from pathlib import Path

from pdf_parser import extract_text_from_pdf

BASE_DIR = Path(__file__).resolve().parents[2]

pdf_path = (
    BASE_DIR /
    "data/resumes/testresume.pdf"
)

resume_text = extract_text_from_pdf(
    pdf_path
)

print(resume_text[:3000])