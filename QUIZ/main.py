from que_model import Question
from data import question_data
from brain import QuizBrain

question_bank = []
for a in question_data:
    que_text = a["text"]
    que_ans = a["answer"]
    x= Question(que_text,que_ans)
    question_bank.append(x)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    
print(f"Thank you for playing \nYour final score is: {quiz.score}/{quiz.question_number}")