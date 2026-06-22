from speech_to_text import generate_transcript

transcript = generate_transcript(
    "backend/interview/answers/answer_9.wav",
    "backend/interview/transcripts/transcript_9.txt",
)

print(transcript)
