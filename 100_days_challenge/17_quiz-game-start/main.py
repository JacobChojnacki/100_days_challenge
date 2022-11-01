from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_data_bank = [Question(x["text"], x["answer"]) for x in question_data]
quiz = QuizBrain(question_data_bank)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")