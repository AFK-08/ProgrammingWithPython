
## Advanced Python Arguments

## Unlimited Arguments:
## Postional Args

def add(sum,*args):     ## *args are in tuple
    for n in args:            
        sum = sum + n
    return sum

result = add(0,3,4,5)
print(result)

## Keyword Args:

def calculate(**kwargs): ## **kwargs are in dictionary
    for n in kwargs:
        print(kwargs[n])

calculate(a=2,b=4)

## some examples:

def cal(n,**kwargs):
    n = n + kwargs["add"]
    n = n * kwargs["mul"]
    print(n)

cal(5,add=5,mul=10)

## We can also pass optional Keyword Arguments in CLasses as well.

## some examples

class Car:
    def __init__(self,**kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

my_car = Car(make="Honda",model="01")
print(my_car.model)

## But if we donot pass Arguments Program will crash, so we use
## get instead of dictionary square brackets so it will return
## None if it didnot find any value

class Car1:
    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car1(make="Honda")
print(my_car.model)
