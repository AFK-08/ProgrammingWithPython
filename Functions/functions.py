print("Hello")
print(len("Hello"))
##len is a built in function. Function has a name and then it is followed by a set of parenthesis.

##What if we want to make our own function according to our requirement or to avoid repeated work.

##To make Function we start with keyword def. which is basically defines a function

def myFunction():
    print("This is my First Function in Python")
    print("Keep Learning Ahmad. You are doing Great.")

myFunction()  #Function Calling

##Functions with Inputs
##Arguments and Parameters

## Parameter: It is the name of data or variable that contains the data that is being passed to it

##Argument is the actual data that is passed to parameter

##You can see in following that "name" is parameter while "Ahmad Farooq Khawaja" is argument

#Example 1
def greet(name):
    print(f"Hello How are you {name}?")
    print(f"How is you doing {name}!")

greet("Ahmad Farooq Khawaja")

##Example 2:
def life_in_weeks(age):
    age=90-age
    age=age*52
    print(f"You have {age} weeks left!")

life_in_weeks(56)

##Function with Multiple Inputs:

def greeting(name,location):
    print(f"Hello {name}")
    print(f"What is it to be like in {location}")

greeting("Ahmad","Pakistan")

##Postional and Keyword Arguments
###Positional Arguments are the by default way of calling the functions,,,,First Argument is assigned to first parameter and 2nd argument is assigned to 2nd Parameter and so on..,,,so we have to put arguments in order to get correct results

##Keyword Arguments..we donot care about order because can assign arguments to parameters in function calling...

##Example:
def greeting_keyword(name,location):
    print(f"Hello {name}")
    print(f"What is it to be like in {location}")

####Now the order of arguments doesnot matter. These are the keyword Arguments
greeting_keyword(location="Pakistan",name="Ahmad")
print("*****************")

## Functions with Outputs

def my_function():
    return 3*10

def my_function2(number):
    return number*10

result=my_function2(my_function())
print(result)
print("***********************")

    















     




