## To construct object from class we use 
## object name = class name()
## Objects has Attributes(Variables or information ) and Methods(Functionality of Object)

## To get Attribute of Object we simply use objectname.AttributeName()


# import turtle
# timmy=turtle.Turtle()

## or
from turtle import Turtle

timmy=Turtle()
timmy.shape("turtle")
timmy.color("red")
print(timmy)
timmy.forward(100)
timmy.home()

## These are the premade classes and objects and attributes made by developers so we are just using them.

## To get Attribute of Object we simply use objectname.AttributeName

from turtle import Screen
my_screen =  Screen()      ## Creating object from _Screen Class

## Accessing Attribut of Object
print(my_screen.canvheight)

## To access methods of object we use   objectName.Methodname()
## Accessing Method of Object( Functionality of Object )

## In below case there is a function premade which says exit screen on click otherwise keep running the program
my_screen.exitonclick()

## Installing and Implementing Python Packages

import prettytable     ## import library
from prettytable import PrettyTable   ## Importing Class
from prettytable import TableStyle    ## Importing Style class
table= PrettyTable()                 ## Creating Object

## Using Attributes to enter the data inside it

table.field_names = ["Name", "City"]
table.add_row(["Ahmad Farooq","Lodhran"])
table.add_row(["Khizar","Lahore"])
table.add_row(["Nadeem","Pakpattan"])
table.title="Students Data"
table.set_style(TableStyle.DEFAULT)
print(table)


