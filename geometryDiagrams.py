import turtle,random
from turtle import Turtle,Screen
timmy=Turtle()
screen=Screen()

colors=["red","green","cyan","blue","yellow","black","grey","orange","purple","magenta","olive","maroon","aqua","beige"]

def draw(sides):
    angle=360/sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)

for sides in range(3,11):
    timmy.color(random.choice(colors))
    draw(sides)


screen.exitonclick()