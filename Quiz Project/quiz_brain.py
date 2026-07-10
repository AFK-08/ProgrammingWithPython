class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0
    
    def still_questions(self):
        return self.question_number<len(self.question_list)
    
    def next_question(self):
        current_question=self.question_list[self.question_number]
        text=current_question.text
        self.question_number += 1
        choice=input(f"Q.{self.question_number}: {text} (True/False)")
        self.check_answer(choice,current_question.answer)
    
    def check_answer(self,choice,correct_answer):
        if choice.lower()==correct_answer.lower():
            print("You got it right!")
            self.score +=1
        else:
            print("You got it wrong!")
        print(f"The correct answer was : {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")





