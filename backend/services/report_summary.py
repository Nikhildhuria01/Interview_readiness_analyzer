from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_summary(role, score, matched, missing):

    prompt = f"""
    Role: {role}

    Readiness Score: {score}

    Matched Skills:
    {matched}

    Missing Skills:
    {missing}

    Generate:

    1. Strengths
    2. Weaknesses
    3. Recommended Learning Path
    4. Final Assessment

    Keep it professional.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
