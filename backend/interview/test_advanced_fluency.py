from advanced_fluency import (
    analyze_advanced_fluency
)

with open(
    "interview/transcript.txt",
    "r",
    encoding="utf-8"
) as f:

    transcript = f.read()

result = analyze_advanced_fluency(
    transcript,
    duration_seconds=15
)

print(result)