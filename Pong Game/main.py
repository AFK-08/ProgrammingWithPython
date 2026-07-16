from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from centerline import Line
import time

## Screen Setup
screen=Screen()
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("maroon")
screen.tracer(0)

## Setting Line up:

line=Line()

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

## Creating Scoreboard 

score=Scoreboard()

game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    ## Detecting Collison with the Wall:
    if ball.ycor()>285 or ball.ycor()<-285:
        ball.bounce_y()
    
    ## Detecting Collision with Paddles:

    if (ball.distance(right_paddle)<50 and ball.xcor()>330) or (ball.distance(left_paddle)<50 and ball.xcor()<-330):
        ball.bounce_x()
    
    ## Detecting Ball missed by Paddles:
    if ball.xcor()>400: 
        ball.reset()
        score.left_points()

    if ball.xcor()<-400:
        ball.reset()
        score.right_points()
    

    
















screen.exitonclick()