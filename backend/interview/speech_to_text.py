import whisper

print(
    "Loading Whisper Model..."
)

model = whisper.load_model(
    "base"
)

print(
    "Converting Speech To Text..."
)

result = model.transcribe(
    "backend/interview/interview_audio.wav"
)

transcript = result["text"]

with open(
    "backend/interview/transcript.txt",
    "w"
) as f:

    f.write(
        transcript
    )

print(
    "\nTranscript Generated Successfully!"
)

print(
    "\nTranscript:"
)

print(
    transcript
)