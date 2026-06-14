from groq import Groq

client = Groq(api_key="")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Generate 5 interview questions on Terraform"}
    ],
)

print(response.choices[0].message.content)
