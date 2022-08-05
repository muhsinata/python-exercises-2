from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question_dictionary in question_data:
    question_obj = Question(question_dictionary["question"], question_dictionary["correct_answer"].lower())
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.current_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
