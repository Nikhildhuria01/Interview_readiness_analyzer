import streamlit as st
import sys
from pathlib import Path

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="AI Interview Readiness Analyzer", page_icon="🚀", layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
<style>

.main {
    background-color: #0E1117;
}

.block-container {
    padding-top: 2rem;
}

h1 {
    text-align: center;
    color: #4CAF50;
}

.stMetric {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 15px;
}

</style>
""",
    unsafe_allow_html=True,
)

# ==================================================
# IMPORT BACKEND
# ==================================================

BASE_DIR = Path(__file__).resolve().parents[1]

sys.path.append(str(BASE_DIR / "backend/services"))

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

# ==================================================
# TITLE
# ==================================================

st.markdown(
    """
    <h1>🚀 AI Interview Readiness Analyzer</h1>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# ==================================================
# INPUT SECTION
# ==================================================

col1, col2 = st.columns(2)

with col1:

    uploaded_file = st.file_uploader("📄 Upload Resume PDF", type=["pdf"])

with col2:

    job_description = st.text_area("💼 Paste Job Description", height=250)

st.markdown("<br>", unsafe_allow_html=True)

analyze = st.button("🔍 Analyze Resume", use_container_width=True)

# ==================================================
# ANALYSIS
# ==================================================

if analyze:

    if uploaded_file is None:

        st.error("Please upload a resume PDF.")

    elif not job_description.strip():

        st.error("Please enter a job description.")

    else:

        try:

            # ==========================================
            # SAVE PDF
            # ==========================================

            temp_path = "temp_resume.pdf"

            with open(temp_path, "wb") as f:

                f.write(uploaded_file.getbuffer())

            # ==========================================
            # EXTRACT PDF TEXT
            # ==========================================

            resume_text = extract_text_from_pdf(temp_path)

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
            # PDF REPORT
            # ==========================================

            generate_report(
                "Software Engineer",
                score,
                resume_skills,
                matched,
                missing,
                role_questions,
                missing_questions,
            )

            # ==========================================
            # RESULTS
            # ==========================================

            st.success("Analysis Complete!")

            st.subheader("🎯 Readiness Score")

            st.progress(min(score / 100, 1.0))

            st.metric("Score", f"{score:.2f}%")

            st.markdown("---")

            # ==========================================
            # SKILLS
            # ==========================================

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("✅ Matched Skills")

                if matched:

                    st.success(", ".join(matched))

                else:

                    st.warning("No matched skills found.")

            with col2:

                st.subheader("❌ Missing Skills")

                if missing:

                    st.error(", ".join(missing))

                else:

                    st.success("No missing skills!")

            st.markdown("---")

            # ==========================================
            # RESUME SKILLS
            # ==========================================

            with st.expander("📄 Resume Skills"):

                for skill in resume_skills:

                    st.write(f"• {skill}")

            # ==========================================
            # JOB SKILLS
            # ==========================================

            with st.expander("💼 Job Skills"):

                for skill in job_skills:

                    st.write(f"• {skill}")

            # ==========================================
            # ROLE QUESTIONS
            # ==========================================

            with st.expander("📚 Role Based Questions"):

                for q in role_questions:

                    st.write(f"• {q}")

            # ==========================================
            # EXISTING SKILL QUESTIONS
            # ==========================================

            with st.expander("✅ Questions From Your Skills"):

                for q in existing_questions:

                    st.write(f"• {q}")

            # ==========================================
            # MISSING SKILL QUESTIONS
            # ==========================================

            with st.expander("❌ Questions For Missing Skills"):

                for q in missing_questions:

                    st.write(f"• {q}")

            st.markdown("---")

            # ==========================================
            # DOWNLOAD REPORT
            # ==========================================

            st.subheader("📥 Download Report")

            with open("Interview_Report.pdf", "rb") as pdf_file:

                st.download_button(
                    label="Download Interview Report",
                    data=pdf_file,
                    file_name="Interview_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )

        except Exception as e:

            st.error(f"Error: {str(e)}")
