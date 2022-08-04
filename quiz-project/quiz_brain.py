class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def check_answer(self, user_answer, correct_answer):
        if 

    def current_question(self):
        chosen_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {chosen_question.text} (True/False)?: ")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)






