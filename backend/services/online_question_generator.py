from groq import Groq
from dotenv import load_dotenv
import os


def generate_online_questions(skill):

    load_dotenv()

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = f"""
    Generate 5 technical interview questions
    for {skill}.

    Return only the questions.
    One question per line.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
