from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time

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

## Creating ball object
ball=Ball()


game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    ## Detecting Collison with the Wall:
    if ball.ycor()>285 or ball.ycor()<-285:
        ball.bounce()
    
    ## Detecting Collision with Paddles:

    













screen.exitonclick()