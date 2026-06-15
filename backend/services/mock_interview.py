from answer_evaluator import evaluate_answer

question = "What is Docker?"

print(question)

answer = input("\nYour Answer:\n")

feedback = evaluate_answer(question, answer)

print("\nFEEDBACK\n")

print(feedback)
