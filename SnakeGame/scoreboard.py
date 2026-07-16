from turtle import Turtle
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.high_score=0
        self.goto(0,260)
        self.hideturtle()
        file=open("data.txt")
        self.high_score = file.read()
        file.close()
        self.update_score()
        
    
    def update_score(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}",  align="center",move=False,font=("Courier",20,"bold"))
    
    def game_over(self):
        
        if self.score >int(self.high_score):
            self.high_score = self.score
            with open("data.txt" ,mode= "w") as file:
                file.write(str(self.high_score))
        self.goto(0,0)
        self.write("GAME OVER!",align="center",move=False,font=("Courier",20,"bold"))


    def increase(self):
        self.clear()
        self.score=self.score+1
        self.update_score()
      
    
    



    


    
