import os
import re

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def calculate_correctness(question, candidate_answer, ideal_answer):

    prompt = f"""
You are a senior technical interviewer.

Evaluate the candidate answer against the ideal answer.

Question:
{question}

Ideal Answer:
{ideal_answer}

Candidate Answer:
{candidate_answer}

Scoring Criteria:

Technical Accuracy = 50%
Completeness = 30%
Relevance = 20%

Return EXACTLY in this format:

Score: <number>

Feedback: <one line feedback>
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        result = response.choices[0].message.content

        score_match = re.search(r"Score:\s*(\d+)", result)

        if score_match:

            score = int(score_match.group(1))

        else:

            score = 50

        feedback_match = re.search(r"Feedback:\s*(.*)", result, re.DOTALL)

        if feedback_match:

            feedback = feedback_match.group(1).strip()

        else:

            feedback = "No feedback generated."

        return {"score": score, "feedback": feedback}

    except Exception as e:

        print(f"Correctness Error: {e}")

        return {"score": 0, "feedback": "Evaluation failed."}
