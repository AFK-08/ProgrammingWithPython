import turtle
from turtle import Turtle,Screen
import pandas

image = "./US States Quiz-Game/blank_states_img.gif"

## Screen Setup
screen = Screen()
screen.title("US States Game")
screen.addshape(image)
turtle.shape(image)

## Setting Window Pop for User to Guess
answer_state = screen.textinput(title="States",prompt="Enter the State Name: ")





turtle.mainloop()