import random
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()

def computer_sum():
    sum_computer=0
    for value in computer_cards:
        sum_computer+=value
    return sum_computer

def user_sum():
    sum_user=0
    for value in user_cards:
        sum_user+=value
    return sum_user

print("Welcome to the Blackjack Game")
choice=input("Do you want to play the game? yes or no")
if choice=="yes":
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    user_cards=[]
    computer_cards=[]
    value=1
    while value<=2:
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        value=value+1
    if computer_sum() or user_sum>21:
        if computer_sum()>21:
            computer_cards.reverse()
            computer_cards.remove(11)
            computer_cards.reverse()
            computer_cards.append(1)
        elif user_sum()>21:
            user_cards.reverse()
            user_cards.remove(11)
            user_cards.reverse()
            user_cards.append(1)
    if computer_sum()==21:
                    print(f"Computer cards: {computer_cards} Current Score: {computer_sum()}")
                    print("Computer has a blackjack. You lose")
                    exit(0)


    another_card="yes"
    while another_card=="yes":
        print(f"Your Cards: {user_cards} , Current Score: {user_sum()}")
        print(f"Computers first card: {computer_cards[0]}")

        another_card=input("Type yes if you want another card?")
        if another_card=="yes":
            new_card=random.choice(cards)
            user_cards.append(new_card)
        if user_sum()>21:
            if new_card==11:
                user_cards.reverse()
                user_cards.remove(11)
                user_cards.reverse()
                user_cards.append(1)
            else:
                print(f"Your Cards: {user_cards} , Current Score: {user_sum()}")
                print("You lose.")
                exit(0)

        if another_card!="yes":
            while computer_sum()<17:
                if computer_sum()<17:
                    new_card=random.choice(cards)
                    computer_cards.append(new_card)
                    if new_card==11 and computer_sum()>21:
                        computer_cards.reverse()
                        computer_cards.remove(11)
                        computer_cards.reverse()
                        computer_cards.append(1)
                if computer_sum()==21:
                    print(f"Computer cards: {computer_cards} Current Score: {computer_sum()}")
                    print("Computer has a blackjack. You lose")
                    exit(0)
            print(f"Computers cards: {computer_cards}, Current Score:  {computer_sum()}")
            if computer_sum()>21:
                    print("You win.")
                    exit(0)

            if user_sum()==21:
                (print("You have a blackjack. You win"))
                exit(0)
            
            if user_sum()==computer_sum():
                print("It's a tie")
            elif user_sum()<computer_sum():
                print("You lose")
            else:
                print("You win")
    print("*********************")







