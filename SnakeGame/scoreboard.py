from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score=0
        self.goto(0,260)
        self.write(f"Score: {self.score}",align="center",move=True,font=("Comic Sans MS",20,"bold"))
    
    def increase(self):
        self.score=self.score+1
        self.write(f"Score: {self.score}",align="center",move=True,font=("Comic Sans MS",20,"bold"))


    


    
