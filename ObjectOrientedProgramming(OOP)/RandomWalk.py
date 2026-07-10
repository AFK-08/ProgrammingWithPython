### Also using concept of Tuples

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




direction=[0,90,180,270]
screen=Screen()

timmy=Turtle()
timmy.pensize(15)
turtle.speed("fastest")
for _ in range(200):
    timmy.color(random_color())
    timmy.setheading(random.choice(direction))
    timmy.forward(30)

    



















screen.exitonclick()