from typing import List
from question_model import Question


class QuizBrain:

    def __init__(self, question_list: List[Question]):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.question_number += 1
        replace = '"'
        answer = input(
            f'Q.{self.question_number}: {self.question_list[self.question_number - 1].text.replace("&quot;", replace)} (True/False)?: ')
        self.check_answer(answer)

    def check_answer(self, user_answer):
        current_question = self.question_list[self.question_number - 1]
        if user_answer == current_question.answer:
            print('Correct')
            self.score += 1
        else:
            print('Wrong')
