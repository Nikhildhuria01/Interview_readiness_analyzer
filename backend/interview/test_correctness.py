from correctness_analysis import (
    calculate_correctness
)

candidate_answer = """
Machine learning is a subset
of artificial intelligence
that learns from data.
"""

ideal_answer = """
Machine learning is a branch
of AI that enables computers
to learn patterns from data
and make predictions.
"""

score = calculate_correctness(
    candidate_answer,
    ideal_answer
)

print(
    "\nCorrectness Score:",
    score
)