import os
def clear_screen():
     os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()
import random
print(""" 
      _______  __   __  _______  _______  _______ 
|       ||  | |  ||       ||       ||       |
|    ___||  | |  ||    ___||  _____||  _____|
|   | __ |  |_|  ||   |___ | |_____ | |_____ 
|   ||  ||       ||    ___||_____  ||_____  |
|   |_| ||       ||   |___  _____| | _____| |
|_______||_______||_______||_______||_______|
      """)
print("Welcome to the Number Guessing game.")
print("I am thinking of number between 1 and 100")
level=input("Choose difficulty level, easy or hard.\n")
guess=random.randint(1,100)
if level=="easy":
     print("You have 10 attempts to guess.")
     number=int(input("Enter the guess: "))
     index=1
     while index<10:
          if number==guess:
               print("You guessed it. You won. ")
               exit(0)
          else:
               if guess>number:
                    print("Too low.")
               else:
                    print("Too High")
               print(f"You have {10-index} attempts left!")
               number=int(input("Guess again."))
               
          index+=1
          

elif level=="hard":
     print("You have 5 attempts to guess.")
     number=int(input("Enter the guess: "))
     index=1
     while index<5:
          if number==guess:
               print("You guessed it. You won. ")
               exit(0)
          else:
               if guess>number:
                    print("Too low.")
               else:
                    print("Too High")
               print(f"You have {5-index} attempts left!")
               number=int(input("Guess again."))
               
          index+=1
if number==guess:
     print("You won!")
else:
     print("You lose.")

