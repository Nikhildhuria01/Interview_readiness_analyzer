import streamlit as st

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

sys.path.append(
    str(BASE_DIR / "backend/services")
)

from pdf_parser import extract_text_from_pdf
from resume_parser import extract_resume_skills
from job_parser import extract_job_skills
from skill_gap import compare_skills
from readiness_score import calculate_score

from question_recommender import (
    get_role_questions,
    get_existing_skill_questions,
    get_missing_skill_questions
)

from report_generator import generate_report


# ==========================================
# UI
# ==========================================

st.title(
    "AI Interview Readiness Analyzer"
)

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

analyze = st.button(
    "Analyze Resume"
)

# ==========================================
# ANALYZE
# ==========================================

if analyze:

    if uploaded_file is None:

        st.error(
            "Please upload a resume PDF."
        )

    elif not job_description.strip():

        st.error(
            "Please enter a job description."
        )

    else:

        try:

            # ==========================================
            # SAVE PDF
            # ==========================================

            temp_path = "temp_resume.pdf"

            with open(
                temp_path,
                "wb"
            ) as f:

                f.write(
                    uploaded_file.getbuffer()
                )

            # ==========================================
            # PDF TEXT
            # ==========================================

            resume_text = (
                extract_text_from_pdf(
                    temp_path
                )
            )

            # ==========================================
            # SKILLS
            # ==========================================

            resume_skills = (
                extract_resume_skills(
                    resume_text
                )
            )

            job_skills = (
                extract_job_skills(
                    job_description
                )
            )

            # ==========================================
            # GAP ANALYSIS
            # ==========================================

            matched, missing = (
                compare_skills(
                    resume_skills,
                    job_skills
                )
            )

            # ==========================================
            # SCORE
            # ==========================================

            score = (
                calculate_score(
                    matched,
                    job_skills
                )
            )

            # ==========================================
            # QUESTIONS
            # ==========================================

            role_questions = (
                get_role_questions(
                    "Software Engineer"
                )
            )

            existing_questions = (
                get_existing_skill_questions(
                    matched
                )
            )

            missing_questions = (
                get_missing_skill_questions(
                    missing
                )
            )

            # ==========================================
            # GENERATE PDF REPORT
            # ==========================================

            generate_report(
                "Software Engineer",
                score,
                resume_skills,
                matched,
                missing,
                role_questions,
                missing_questions
            )

            # ==========================================
            # DISPLAY RESULTS
            # ==========================================

            st.success(
                "Analysis Complete"
            )

            st.metric(
                "Readiness Score",
                f"{score:.2f}%"
            )

            # ==========================================
            # SKILLS
            # ==========================================

            st.subheader(
                "Resume Skills"
            )

            st.write(
                resume_skills
            )

            st.subheader(
                "Job Skills"
            )

            st.write(
                job_skills
            )

            st.subheader(
                "Matched Skills"
            )

            st.write(
                matched
            )

            st.subheader(
                "Missing Skills"
            )

            st.write(
                missing
            )

            # ==========================================
            # ROLE QUESTIONS
            # ==========================================

            st.subheader(
                "Role Based Questions"
            )

            for q in role_questions:

                st.write(
                    f"• {q}"
                )

            # ==========================================
            # EXISTING SKILL QUESTIONS
            # ==========================================

            st.subheader(
                "Questions From Your Skills"
            )

            for q in existing_questions:

                st.write(
                    f"• {q}"
                )

            # ==========================================
            # MISSING SKILL QUESTIONS
            # ==========================================

            st.subheader(
                "Questions For Missing Skills"
            )

            for q in missing_questions:

                st.write(
                    f"• {q}"
                )

            # ==========================================
            # DOWNLOAD REPORT
            # ==========================================

            st.subheader(
                "Download Report"
            )

            with open(
                "Interview_Report.pdf",
                "rb"
            ) as pdf_file:

                st.download_button(
                    label="Download Interview Report",
                    data=pdf_file,
                    file_name="Interview_Report.pdf",
                    mime="application/pdf"
                )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )