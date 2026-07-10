import turtle
from turtle import Turtle,Screen
import random
screen=Screen()
color_list=[(234, 233, 231), (230, 233, 238), (237, 231, 234), (227, 234, 230), (203, 161, 90), (59, 89, 128), (141, 90, 44), (136, 173, 197), (135, 27, 50), (220, 207, 113), (153, 53, 84), (35, 42, 67), (169, 157, 43), (45, 55, 103), (132, 186, 144)]

turtle.colormode(255)

def random_color():
    color_num=random.randint(0,14)
    return color_list[color_num]

timmy=Turtle()
timmy.speed("fastest")
timmy.setheading(225)
timmy.hideturtle()
timmy.penup()
timmy.forward(300)
timmy.setheading(0)
timmy.pendown()
for _ in range(10):
    skip=random.randint(1,10)
    for index in range(10):
        if skip!=index:
            color=random_color()
            timmy.dot(20,color)
            timmy.penup()
            timmy.forward(50)
            timmy.pendown()
        else:
            timmy.penup()
            timmy.forward(50)
            timmy.pendown()

            pass
    timmy.penup()
    timmy.left(90)
    timmy.forward(30)
    timmy.left(90)
    timmy.forward(500)
    timmy.left(180)
    timmy.pendown()





























screen.exitonclick()