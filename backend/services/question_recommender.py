from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

# Load interview questions dataset
questions_df = pd.read_csv(
    BASE_DIR / "data/raw/full_interview_questions_dataset.csv", encoding="latin1"
)

# ==================================================
# ROLE BASED QUESTIONS
# ==================================================


def get_role_questions(role, n=5):

    role_questions = questions_df[questions_df["role"].str.lower() == role.lower()]

    return role_questions["question"].head(n).tolist()


# ==================================================
# SKILL QUESTION BANK
# ==================================================

SKILL_QUESTIONS = {
    "Python": [
        "What are Python decorators?",
        "Explain generators in Python.",
        "Difference between list and tuple.",
        "What is GIL in Python?",
    ],
    "Java": [
        "Explain JVM.",
        "Difference between JDK and JRE.",
        "What is method overloading?",
        "Difference between abstract class and interface?",
    ],
    "Linux": [
        "What is Linux Kernel?",
        "Difference between process and thread.",
        "Explain chmod command.",
        "What is a shell?",
    ],
    "Docker": [
        "What is Docker?",
        "Difference between Docker and Virtual Machine.",
        "What is a Docker Image?",
        "Explain Docker Volumes.",
    ],
    "AWS": [
        "What is EC2?",
        "Difference between ECS and EKS.",
        "What is S3?",
        "Explain Auto Scaling.",
    ],
    "Kubernetes": [
        "What is Kubernetes?",
        "What is a Pod?",
        "Difference between Deployment and StatefulSet.",
        "What are ConfigMaps?",
    ],
    "Git": [
        "What is Git?",
        "Difference between merge and rebase.",
        "What is git stash?",
        "Explain pull request workflow.",
    ],
    "SQL": [
        "What is normalization?",
        "Difference between WHERE and HAVING.",
        "What are joins?",
        "Explain indexing.",
    ],
    "Machine Learning": [
        "What is overfitting?",
        "Difference between supervised and unsupervised learning.",
        "Explain cross validation.",
        "What is bias-variance tradeoff?",
    ],
    "Data Science": [
        "What is feature engineering?",
        "Difference between mean and median.",
        "Explain EDA.",
        "What is data cleaning?",
    ],
}
# ==================================================
# GENERIC QUESTIONS FOR UNKNOWN SKILLS
# ==================================================

def generate_generic_questions(skill):

    return [

        f"What is {skill}?",

        f"What are the key features of {skill}?",

        f"Where is {skill} commonly used?",

        f"What are the advantages of {skill}?",

        f"Explain a real-world project using {skill}?"
    ]


# ==================================================
# EXISTING SKILL QUESTIONS
# ==================================================

def get_existing_skill_questions(skills):

    questions = []

    for skill in skills:

        if skill in SKILL_QUESTIONS:

            questions.extend(
                SKILL_QUESTIONS[skill][:2]
            )

        else:

            questions.extend(
                generate_generic_questions(skill)[:2]
            )

    return questions


# ==================================================
# MISSING SKILL QUESTIONS
# ==================================================

def get_missing_skill_questions(skills):

    questions = []

    for skill in skills:

        if skill in SKILL_QUESTIONS:

            questions.extend(
                SKILL_QUESTIONS[skill]
            )

        else:

            questions.extend(
                generate_generic_questions(skill)
            )

    return questions

