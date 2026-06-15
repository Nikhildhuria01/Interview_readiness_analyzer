from answer_evaluator import evaluate_answer

question = "What is Docker?"

answer = "Docker is used to create containers."

feedback = evaluate_answer(question, answer)

print(feedback)
