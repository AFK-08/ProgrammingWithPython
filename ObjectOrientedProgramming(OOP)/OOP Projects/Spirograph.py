import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

screen=Screen()
screen.title("Spirograph")
screen.bgcolor("white")
timmy=Turtle()
timmy.speed("fastest")
timmy.pensize(1.2)

# for _ in range(int(360/5)):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.circle(0,extent=5)

####or*****************

def drawSpirograph(gap_size):
    for _ in range(int(360/gap_size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+gap_size)

drawSpirograph(3)




screen.exitonclick()