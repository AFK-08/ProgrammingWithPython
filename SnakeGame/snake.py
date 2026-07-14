STARTING_POSITIONS =[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
from turtle import Turtle

class Snake:
    ## IT means what should happen when we create snake object..
    def __init__(self):

        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    
    ## Creating Snake body
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    
    def add_segment(self,position):
        new_segment=Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    ## Extending the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())

    ## Moving the snake
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    ## Controlling Snake
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
        else:
            pass
    
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
        else:
            pass

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
        else:
            pass

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
        else:
            pass
    



        
