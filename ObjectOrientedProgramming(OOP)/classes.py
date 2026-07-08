## Creating Own Classes in Python
## Class is basically the blueprint for creating objects
## Class name must be in PascalCase

class User:                ## Creating 1st class but empty
    pass
user_1=User()               ## Creating object from class

## Adding Attributes for the object

user_1.username="Ahmad"    ## Attribute is just variable but
                           ## associated with object
user_1.health=100
"""
But what if we have multiple users and we have add attributes for all the users and we can have error in nameing. Instead we can make them in class using constructors so that when we create or initialize the object they automatically comes with them 
"""
## Creating the Constructor
class Car:
    def __init__(self):
        print("New car being developed.")

## Whenever new object being created, this function will be triggered and so the attributes in this functions will be triggered.

car_1=Car()
car_2=Car()

class Students:
    def __init__(self,id,name):
        self.id=id
        self.name=name            ## Creating Attributes
        self.followers=0
    
    def shuffle(self,student):          ## Creating Methods
        self.id="00"
        student.id="99"

student_1= Students("001","Ahmad Farooq")
student_2=Students("002","Talha Zohaib")
print(student_1.id)
print(student_1.name)
print(student_1.followers)

student_1.shuffle(student_2)
print(student_1.id)
print(student_2.id)
