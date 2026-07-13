import turtle,random
from turtle import Turtle,Screen
screen=Screen()
screen.setup(width=600,height=600)
race_on=False

user_guess =screen.textinput(title="Turtle Race",prompt="Which color Turtle will win?")
colors=["red","yellow","orange","green","blue","purple"]

A=Turtle(shape="turtle")
B=Turtle(shape="turtle")
C=Turtle(shape="turtle")
D=Turtle(shape="turtle")
E=Turtle(shape="turtle")
F=Turtle(shape="turtle")
list=[A,B,C,D,E,F]

direction=-150
index=0

for object in list:
    object.color(colors[index])
    object.penup()
    object.goto(x=-280,y=direction)
    direction=direction+60
    index+=1

if user_guess:
    race_on=True

while race_on:

    for object in list:

        if object.xcor()>280:
            race_on=False
            winner=object.pencolor()
            if winner==user_guess:
                print(f"You won! The {winner} color turtle won the race")
            else:
                print(f"You lose! The {winner} color turtle won the race")

        random_num=random.randint(0,10)
        object.forward(random_num)

screen.exitonclick()