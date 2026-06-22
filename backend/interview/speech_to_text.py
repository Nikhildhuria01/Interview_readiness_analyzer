import whisper

print("Loading Whisper Model Once...")

model = whisper.load_model("tiny")

print("Whisper Ready!")


def generate_transcript(audio_file, transcript_file):

    result = model.transcribe(audio_file)

    transcript = result["text"]

    with open(transcript_file, "w", encoding="utf-8") as f:

        f.write(transcript)

    return transcript
