import turtle,random,time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Score

## Screen Setup for Game.
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)

timing=0.1
level=screen.textinput(title="Snake Level" ,prompt="choose level: easy, medium, hard: ")

## Level Check
if level=="easy":
    timing=0.3
elif level=="medium":
    timing=0.2
elif level=="hard":
    timing=0.1

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)

## Moving the snake

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(timing)
    snake.move()

    ## Detect Collision with Food
    if snake.head.distance(food)<15:
        snake.extend()
        food.move()
        score.increase()
    
    ## Detect Collision with the Wall:
    if snake.head.xcor()>295 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-295:
        score.game_over()
        game_is_on=False
    

    ## Detect Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over()
    

        

        






    














screen.exitonclick()









