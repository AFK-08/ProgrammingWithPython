def add(n1,n2):
    return n1+n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def subtract(n1,n2):
    return n1-n2
print("Welcome to the Calculator")
num1=int(input("What is the first number: "))
value='y'
while value=='y':
    operation=input("Which operation you want to perform: + - * / ")
    num2=int(input("Enter the 2nd number: "))
    if operation=='+':
         result=add(num1,num2)
    elif operation=='-':
         result=subtract(num1,num2)
    elif operation=="*":
         result=multiply(num1,num2)
    elif operation=='/':
         result=divide(num1,num2)
    print(f"Answer is : {result}")
    value=input("type y to continue calculation and n for not")
    if value=='y':
        num1=result
    else:
        print("Good Buy")



