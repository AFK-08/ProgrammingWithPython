import turtle as t
from turtle import Turtle,Screen
screen=Screen()
timmy=Turtle()
timmy.pensize(5)
timmy.pencolor("green")

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def move_clockwise():
    timmy.right(10)

def move_anticlockwise():
    timmy.left(10)

def clear_screen():
    screen.reset()
    timmy.pensize(5)
    timmy.pencolor("green")

screen.listen()
screen.onkeypress(fun=move_forward,key="w")
screen.onkeypress(fun=move_backward,key="s")
screen.onkeypress(fun=move_clockwise,key="d")
screen.onkeypress(fun=move_anticlockwise,key="a")
screen.onkey(fun=clear_screen,key="c")


screen.exitonclick()


