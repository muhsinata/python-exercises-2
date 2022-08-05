class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def current_question(self):
        chosen_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {chosen_question.text} (True/False)?: ")
        self.check_answer(user_answer, chosen_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You're right! {self.score}/{self.question_number}")
        else:
            print(f"You're wrong! {self.score}/{self.question_number}")
        print("\n")
