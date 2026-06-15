from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def evaluate_answer(question, answer):

    prompt = f"""
    You are a technical interviewer.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer.

    Give:

    Technical Accuracy (0-10)

    Completeness (0-10)

    Clarity (0-10)

    Overall Score (0-10)

    Missing Concepts

    Improvement Suggestions
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
