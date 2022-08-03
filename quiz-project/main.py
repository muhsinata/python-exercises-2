from data import question_data
from question_model import Question

score = 0
question = 0
for question in question_data:
    question = Question(question["text"], question["answer"])
    print(question.text)
    answer = input("True or False: ")
    question += 1
    if answer == question.answer:
        score += 1
        print(f"Success: {score}/{question}")

