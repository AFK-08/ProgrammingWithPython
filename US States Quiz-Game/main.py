import turtle
from turtle import Turtle,Screen
import pandas

image = "./US States Quiz-Game/blank_states_img.gif"
data = pandas.read_csv("./US States Quiz-Game/50_states.csv")

## Creating Turtle Object which write state names on map
state = Turtle()
state.hideturtle()
state.penup()

## Screen Setup
screen = Screen()
screen.title("US States Game")
screen.addshape(image)
turtle.shape(image)


guessed_states=[]

while len(guessed_states)<50:

    ## Setting Window Pop for User to Guess
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed" ,prompt="Enter the State Name or Type Exit" )
    answer_state = answer_state.title()

    if answer_state=="Exit":
        break

    ## Manipulating data from csv
    states_list = data.state.to_list()
    state_row = data[data.state==answer_state]

    if answer_state in states_list:

        ## item() method fetches first element of series column
        x_coordiante = state_row.x.item()
        y_coordinate = state_row.y.item()
        state.goto(x_coordiante,y_coordinate)
        state.write(answer_state)
        guessed_states.append(answer_state)

## Creating CSV file for user to learn what he missed.

missing_states= [states for states in states_list if states not in guessed_states]

learn = pandas.DataFrame(missing_states)
learn.to_csv("./US States Quiz-Game/learn.csv")


