import turtle,random,time
from turtle import Turtle,Screen
from snake import Snake

## Screen Setup for Game.
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)

## Moving the snake

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    














screen.exitonclick()









