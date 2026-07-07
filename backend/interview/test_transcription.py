from speech_to_text import generate_transcript

transcript = generate_transcript(
    "interview/answers/answer_9.wav",
    "interview/transcripts/transcript_9.txt",
)

print(transcript)
