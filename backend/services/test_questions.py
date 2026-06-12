from question_recommender import get_questions

questions = get_questions(
    "Software Engineer",
    n=5
)

for q in questions:
    print(q)