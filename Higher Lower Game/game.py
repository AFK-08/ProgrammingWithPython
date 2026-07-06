import random
import data
import os
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
clear_screen()

dictionary_A={}
dictionary_B={}
print("Welcome to the Higher Lower game!")
dictionary_A=random.choice(data.data)
dictionary_B=random.choice(data.data)
answer=True
score=0
while answer==True:
  
    while dictionary_A==dictionary_B:
        dictionary_B=random.choice(data.data)
    print(f"Compare A: {dictionary_A["name"]}, a {dictionary_A["description"]}, from {dictionary_A["country"]}")
    print("\n\nVS\n\n")
    print(f"Against B: {dictionary_B["name"]}, a {dictionary_B["description"]}, from {dictionary_B["country"]}")
    
    choice=input("Who has more followers.\n Type 'A' or 'B': ")
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
    dictionary_A=dictionary_B
    dictionary_B=random.choice(data.data)