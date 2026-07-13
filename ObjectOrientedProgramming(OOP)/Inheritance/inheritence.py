## Class Inheritance

## Classes can inherit from another classes, their Attributes and
## Methods, Let's see how class inheritance works!

## Understand What it means:
### Imagine you work for A Resturant

"""*** Lets say you code up a robot CHEF which can 

       bake(), measure(), stir()

       And resturant says we also now need of PASTRY CHEF 
       which can now knead the dhough and whisk the eggs
       and also do the work that a normal chef does. SO instead of 
       writing code from scratch you INHERIT the attributes and Functionality from another class which is CHEF and add
       another things. SO now PASTRY CHEF can do:

       bake(), measure(), stir(), knead(), whisk()

       That's what Inheritance is in FIRST PLACE.
"""

### SEE CODE EXAMPLE BELOW:

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, Exhale")


class Fish(Animal):
    ## Inherting Animal class
    def __init__(self):
        super().__init__()
        self.have_legs = False
    
    def swim(self):
        print("We can Swim.")

    ## Can also modify the method of super class:
    
    def breath(self):
        super().breath()
        print("doing this underwater")

###********************************************************

fish = Fish()
fish.swim()

## Let's say we inherit Animal class for the Fish class as we want to add attributes and funcionality of Animal class in fish class also.

## We inherit as : class Fish(Animal):
## And in init function we use:
## super().__init__()

fish.breath()
print(fish.num_eyes)


