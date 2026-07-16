from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.pensize(5)
        self.setheading(90)
        self.forward(300)
        self.index=1
        while self.index<=60:
            if self.index%2==0:
                self.penup()
            else:
                self.pendown()
            self.index+=1
            self.backward(10)
