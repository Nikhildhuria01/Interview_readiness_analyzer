import sounddevice as sd
from scipy.io.wavfile import write

DURATION = 15

SAMPLE_RATE = 44100

print(
    "Recording Started..."
)

recording = sd.rec(
    int(
        DURATION * SAMPLE_RATE
    ),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="int16"
)

sd.wait()

write(
    "backend/interview/interview_audio.wav",
    SAMPLE_RATE,
    recording
)

print(
    "Recording Saved!"
)