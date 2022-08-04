from data import question_data
from question_model import Question

score = 0
number_of_question = 0
for question in question_data:
    question = Question(question["text"], question["answer"].lower())
    print(question.text)
    answer = input("True or False: ").lower()
    number_of_question += 1
    if answer == question.answer:
        score += 1
    print(f"Success: {score}/{number_of_question}")

