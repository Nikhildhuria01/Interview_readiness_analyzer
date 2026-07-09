import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_transcript(audio_file, transcript_file):

    with open(audio_file, "rb") as file:

        transcription = client.audio.transcriptions.create(
            file=file,
            model="whisper-large-v3-turbo",
            response_format="text",
            language="en",
        )

    transcript = transcription

    with open(transcript_file, "w", encoding="utf-8") as f:
        f.write(transcript)

    return transcript
