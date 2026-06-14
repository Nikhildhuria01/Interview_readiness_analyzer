from groq import Groq

client = Groq(api_key="")


def generate_online_questions(skill):

    prompt = f"""
    Generate 5 technical interview questions
    for {skill}.

    Return only the questions.
    One question per line.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
