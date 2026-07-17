# FOR LOOP IN THE LISTS/ RANGE FUNCTION

fruits=["Apple","Orange","Mango"]
for fruit in fruits:
    print(fruit)
    print(fruit+" pie")
print(fruits)
print(fruit)   
             #VARIABLE VALUE UPDATED EACH TIME A  LOOP RUNS SO FRUIT CONTAINS MANGO, DRY RUN THE LOOP TO SEE WHAT'S HAPPENING BEHIND THE SCENES


numbers=[1,2,3,"Ahmad"]
for item in numbers:
    print(item)




#FIND SUM OF ALL NUMBERS IN A LIST
scores=[5,5,10,20,50]

print(sum(scores))           #BUILT IN SUM FUNCTION

#MANUAL LOGIC

sum=0
for number in scores:
    sum=sum + number
print(sum)


#FIND HIGHEST IN A LIST
marks=[10,20,25,12,13]
highest=0
for number in marks:
    if number>highest:
        highest=number
print(highest)


#FOR LOOP AND RANGE FUNCTION

print(range(1,10)) 
                    # Range doesnot work independently, it works with conjuction of another function..like this simply prints the range(1,10) but using it with for loops actually gives our     required result.


for number in range(1,10):
    print(number)            
                     #In range function,end of range like 10 is not included.In range function each time loop runs it by default add 1 to previous one but if you want to jump and add some other number to it you can simply use this.

for number in range(1,10,2):
    print(number)


#FIND TOTAL SUM IN RANGE
total=0
for number in range(1,101):
    total=total+number
print(total)

#FIZZBUZZ GAME IN PYTHON
#RULES:
#You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:Your program should print each number from 1 to 100 in turn and include number 100.But when the number is divisible by 3 then instead of printing the number it should print "Fizz".When the number is divisible by 5, then instead of printing the number it should print "Buzz".`And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1,101):
    if (number%3==0 and number%5==0):
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)










    
    