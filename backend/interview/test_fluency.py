from fluency_analysis import (
    analyze_fluency
)

with open(
    "backend/interview/transcript.txt",
    "r",
    encoding="utf-8"
) as f:

    transcript = f.read()

result = analyze_fluency(
    transcript
)

print("\nFluency Analysis:")
print(result)