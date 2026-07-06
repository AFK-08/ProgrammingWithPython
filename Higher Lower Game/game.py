import random
import data
import os
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
clear_screen()

dictionary_A={}
dictionary_B={}
print("Welcome to the Higher Lower game!")

##Getting two dictionaries from list

dictionary_A=random.choice(data.data)
dictionary_B=random.choice(data.data)
answer=True
score=0
while answer==True:
    ## Validating that dictionaries must not be same

    while dictionary_A==dictionary_B:
        dictionary_B=random.choice(data.data)
    ## Comparing the dictionaries
    print(f"Compare A: {dictionary_A["name"]}, a {dictionary_A["description"]}, from {dictionary_A["country"]}")
    print("\n\nVS\n\n")
    print(f"Against B: {dictionary_B["name"]}, a {dictionary_B["description"]}, from {dictionary_B["country"]}")

    ##Asking users their guess

    choice=input("Who has more followers.\n Type 'A' or 'B': ")

    ##Checking Answers

    if dictionary_A["follower_count"]>dictionary_B["follower_count"] and choice=="A":
        answer=True
        clear_screen()

    elif dictionary_B["follower_count"]>dictionary_A["follower_count"] and choice=="B":
        answer=True
        clear_screen()
    else:
        answer=False
        print(f"You lose. Final Score:  {score}")
    score=score+1
    if answer==True:
        print(f"You are Right. Current Score: {score}")

    ## Putting dictionary B into A and then updating dictionary B
    
    dictionary_A=dictionary_B
    dictionary_B=random.choice(data.data)