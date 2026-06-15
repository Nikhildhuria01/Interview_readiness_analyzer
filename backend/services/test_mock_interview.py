from answer_evaluator import evaluate_answer

questions = [
    ("What is Docker?", "Docker is a platform used to build and run containers."),
    (
        "Explain Git branching.",
        "Git branching allows developers to work on features independently.",
    ),
    ("What is Kubernetes?", "Kubernetes is a container orchestration platform."),
]

for i, (question, answer) in enumerate(questions, start=1):

    print(f"\n{'='*50}")
    print(f"QUESTION {i}")
    print(f"{'='*50}")

    print(question)

    print("\nANSWER:")
    print(answer)

    print("\nFEEDBACK:")

    feedback = evaluate_answer(question, answer)

    print(feedback)
