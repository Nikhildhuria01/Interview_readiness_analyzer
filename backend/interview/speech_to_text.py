from faster_whisper import WhisperModel
import os

print("Loading Faster-Whisper Model...")

model = WhisperModel(
    "tiny",
    device="cpu",
    compute_type="int8"
)

print("Faster-Whisper Ready!")


def generate_transcript(audio_file, transcript_file):

    segments, info = model.transcribe(
        audio_file,
        beam_size=1
    )

    transcript = " ".join(
        segment.text
        for segment in segments
    ).strip()

    os.makedirs(
        os.path.dirname(transcript_file),
        exist_ok=True
    )

    with open(
        transcript_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(transcript)

    return transcript