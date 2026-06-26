print("Welcome to Python Pizza Deliveries!")
size = str(input("What size pizza do you want? S, M or L: "))
pepp = str(input("Do you want pepperoni on your pizza? Y or N: "))
cheese = str(input("Do you want extra cheese? Y or N: "))
bill=0
if size=='S':
    bill=15
elif size=='M':
    bill=20
else:
    bill=25
if pepp=='Y':
    if size=='S':
        bill=bill+2
    else:
        bill=bill+3
if(cheese=='Y'):
    bill=bill+1
print(bill)

