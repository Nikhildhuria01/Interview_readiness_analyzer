import re

def analyze_fluency(text):

    words = text.split()

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
                text.lower()
            )
        )

    fluency_score = max(
        0,
        100 - (filler_count * 10)
    )

    return {

        "word_count": word_count,

        "filler_count": filler_count,

        "fluency_score": fluency_score
    }