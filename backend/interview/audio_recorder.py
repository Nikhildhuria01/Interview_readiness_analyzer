import sounddevice as sd
from scipy.io.wavfile import write


def record_answer(
    filename,
    duration=10
):

    SAMPLE_RATE = 44100

    print(
        "\nRecording Started..."
    )

    recording = sd.rec(
        int(
            duration * SAMPLE_RATE
        ),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(
        filename,
        SAMPLE_RATE,
        recording
    )

    print(
        f"Recording Saved: {filename}"
    )