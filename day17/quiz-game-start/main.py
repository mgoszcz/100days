from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(question.get('question'), question.get('correct_answer')) for question in question_data]

# for question in question_bank:
#     print(question.text, question.answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    print(f'Your current score is: {quiz.score} / {quiz.question_number}')

print(f'Your final score is: {quiz.score} / {len(question_bank)}')
