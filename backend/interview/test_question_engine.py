from question_engine import generate_interview_questions

resume_skills = ["Python", "Docker", "AWS"]

jd_skills = ["Python", "Docker", "AWS", "Kubernetes", "CI/CD", "Jenkins"]

questions = generate_interview_questions(resume_skills, jd_skills)

for i, q in enumerate(questions, start=1):

    print(f"{i}. {q}")
