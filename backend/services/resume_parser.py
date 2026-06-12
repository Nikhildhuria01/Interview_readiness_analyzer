import re
from skills import TECH_SKILLS

def extract_resume_skills(resume_text):

    skills_found = []

    for skill in TECH_SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(
            pattern,
            resume_text,
            re.IGNORECASE
        ):
            skills_found.append(skill)

    return skills_found