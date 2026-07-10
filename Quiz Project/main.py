from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import os 
def clear_screen():
    os.system("cls" if os.name=='nt' else 'clear')
clear_screen()

question_bank=[]
for item in question_data:
    question=Question(item["text"],item["answer"])
    question_bank.append(question)

quiz=QuizBrain(question_bank)
while quiz.still_questions():
    quiz.next_question()
print("You have Completed the Quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")







