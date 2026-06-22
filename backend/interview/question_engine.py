import sys
from pathlib import Path
import random

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from backend.services.question_recommender import (
    get_existing_skill_questions,
    get_missing_skill_questions,
)

BEHAVIORAL_QUESTIONS = [
    "Tell me about yourself.",
    "Describe a challenging project you worked on.",
    "Why should we hire you?",
    "Tell me about a time you solved a difficult problem.",
    "Describe a conflict in your team and how you handled it.",
]


def generate_interview_questions(resume_skills, jd_skills):

    # =========================
    # SKILL GAP
    # =========================

    skill_gaps = [skill for skill in jd_skills if skill not in resume_skills]

    # =========================
    # RESUME QUESTIONS
    # =========================

    resume_questions = get_existing_skill_questions(resume_skills)

    random.shuffle(resume_questions)

    resume_questions = resume_questions[:4]

    # =========================
    # JD QUESTIONS
    # =========================

    jd_questions = get_existing_skill_questions(jd_skills)

    random.shuffle(jd_questions)

    jd_questions = jd_questions[:3]

    # =========================
    # GAP QUESTIONS
    # =========================

    gap_questions = get_missing_skill_questions(skill_gaps)

    random.shuffle(gap_questions)

    gap_questions = gap_questions[:2]

    # =========================
    # BEHAVIORAL
    # =========================

    behavioral = [random.choice(BEHAVIORAL_QUESTIONS)]

    # =========================
    # COMBINE
    # =========================

    final_questions = resume_questions + jd_questions + gap_questions + behavioral

    # =========================
    # REMOVE DUPLICATES
    # =========================

    final_questions = list(dict.fromkeys(final_questions))

    random.shuffle(final_questions)

    # =========================
    # ENSURE 10 QUESTIONS
    # =========================

    while len(final_questions) < 10:

        extra_question = random.choice(BEHAVIORAL_QUESTIONS)

        if extra_question not in final_questions:

            final_questions.append(extra_question)

    return final_questions[:10]
