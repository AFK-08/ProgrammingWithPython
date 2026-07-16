import turtle
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,XPOS):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.goto(XPOS,0)


    def up(self):
        self.forward(12)
    def down(self):
        self.backward(12)

        
        


