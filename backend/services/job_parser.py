import re
from skills import TECH_SKILLS

def extract_job_skills(job_text):

    skills_found = []

    for skill in TECH_SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(
            pattern,
            job_text,
            re.IGNORECASE
        ):
            skills_found.append(skill)

    return skills_found