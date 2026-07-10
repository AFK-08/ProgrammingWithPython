import turtle
from turtle import Turtle,Screen
import random

colors=["red","green","cyan","blue","yellow","black","grey","orange","purple","magenta","maroon","aqua"]
direction=[0,90,180,270]
screen=Screen()
timmy=Turtle()
timmy.pensize(15)
turtle.speed("fastest")
for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.setheading(random.choice(direction))
    timmy.forward(30)

    



















screen.exitonclick()