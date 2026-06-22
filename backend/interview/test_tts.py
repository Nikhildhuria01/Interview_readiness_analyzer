import pyttsx3
import time

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty(
    "voice",
    voices[17].id  # Daniel
)

for i in range(1, 11):

    print(f"Question {i}")

    engine.say(
        f"This is question {i}"
    )

    engine.runAndWait()

    time.sleep(1)

engine.stop()