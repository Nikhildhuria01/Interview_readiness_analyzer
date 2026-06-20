import re

def analyze_advanced_fluency(
    transcript,
    duration_seconds=15
):

    words = transcript.split()

    word_count = len(words)

    filler_words = [
        "um",
        "uh",
        "like",
        "actually",
        "you know"
    ]

    filler_count = 0

    for filler in filler_words:

        filler_count += len(
            re.findall(
                filler,
                transcript.lower()
            )
        )

    words_per_minute = round(
        (word_count / duration_seconds) * 60,
        2
    )

    repeated_words = 0

    for i in range(
        len(words) - 1
    ):

        if (
            words[i].lower()
            ==
            words[i+1].lower()
        ):

            repeated_words += 1

    fluency_score = max(

        0,

        100
        - (filler_count * 10)
        - (repeated_words * 5)

    )

    return {

        "word_count": word_count,

        "filler_count": filler_count,

        "words_per_minute":
            words_per_minute,

        "repeated_words":
            repeated_words,

        "fluency_score":
            fluency_score
    }