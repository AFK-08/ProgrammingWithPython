import random
print("Welcome to the Blackjack Game")
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards=[]
computer_cards=[]
value=1
while value<=2:
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    value=value+1
print(user_cards)
print(computer_cards[0])
print("*********************")

sum_computer=0
for value in computer_cards:
    sum_computer+=value

sum_user=0
for value in user_cards:
    sum_user+=value

print(sum_computer)
print("**********************")
if sum_computer==21:
    print(computer_cards)
    print("Computer gets a blackjack. You lose")


