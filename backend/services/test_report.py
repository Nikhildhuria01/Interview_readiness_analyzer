from report_generator import generate_report

generate_report(
    role="Software Engineer",
    readiness_score=65,
    resume_skills=["Linux", "Git", "Docker"],
    matched=["Linux", "Git"],
    missing=["Python", "Jenkins"],
    role_questions=["What is polymorphism?", "Difference between stack and queue?"],
    missing_questions=["What are Python decorators?", "Explain Jenkins pipeline."],
)
