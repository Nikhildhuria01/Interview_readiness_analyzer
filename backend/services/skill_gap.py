def compare_skills(
    resume_skills,
    job_skills
):

    matched = []

    missing = []

    for skill in job_skills:

        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing