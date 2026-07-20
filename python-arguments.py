
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