import turtle,random,time
from turtle import Turtle,Screen

## Screen Setup for Game.
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)

## Creating a snake body.
segments=[]
positions=[(0,0),(-20,0),(-40,0)]

for position in positions:
    new_segment=Turtle(shape="square")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

## Moving the snake
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg in range(len(segments)-1,0,-1):
        new_x=segments[seg-1].xcor()
        new_y=segments[seg-1].ycor()
        segments[seg].goto(new_x,new_y)
        
    segments[0].forward(20)












screen.exitonclick()









