#Generate Strong Passwords include letters,symbols,numbers.
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")
letterNo=int(input("How many letters you want in Password?\n"))
numbersNo=int(input("How many Numbers you want in password?\n"))
symbolsNo=int(input("How many symbols you want in password?\n"))

#To make the sequence of password also random i use lists not strings so i can easily manipulate them. We choose letters randomly then numbers and then symbols.

lettersstr=[]
for letter in range(1,letterNo+1):
    letter=random.choice(letters)
    lettersstr.append(letter)

numberstr=[]
for number in range(1,numbersNo+1):
    number=random.choice(numbers)
    numberstr.append(number)

symbolstr=[]
for symbol in range(1,symbolsNo+1):
    symbol=random.choice(symbols)
    symbolstr.append(symbol)

# This was the hard part. I made 3 lists together into one list and then apply a random function on list and then change it to string.

#BUT THERE WAS A PROBLEM. WHEN I USE RANDOM FUNCTION ON A FINAL LIST IT CAN CHOOSE RANDOMLY THE SAME CHARACTER SKIPPING SOME CHARACTERS SO I USED THE REMOVE FUNCTION OF LIST SO THAT IF ONE CHARACTER IS USED, IT SHOULD NEVER BE USE AGAIN. THAT WAS ALL.

#I FIGURED OUT FINALLY.


lettersstr.extend(numberstr)
lettersstr.extend(symbolstr)

password=""
for item in range(1,1+letterNo+numbersNo+symbolsNo):
    item1=random.choice(lettersstr)
    password=password+item1
    lettersstr.remove(item1)

print("Your Password is:",password)