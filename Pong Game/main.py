from turtle import Screen,Turtle
from paddle import Paddle

## Screen Setup
screen=Screen()
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)

## Creating Paddle
right_paddle=Paddle(360)
left_paddle=Paddle(-360)


## Moving Paddles

screen.listen()
screen.onkeypress(fun=left_paddle.up,key="w")
screen.onkeypress(fun=left_paddle.down,key="s")
screen.onkeypress(fun=right_paddle.up,key="Up")
screen.onkeypress(fun=right_paddle.down,key="Down")

game_on=True
while game_on:
    screen.update()













screen.exitonclick()