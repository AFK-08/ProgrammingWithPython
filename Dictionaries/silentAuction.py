## Using Dictionary Concepts

import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') ##Clear Screen

value="yes"
data_dictionary={}
while value=='yes':
    name=input("What is your name: ")
    bid=int(input("What is your bid: "))
    user_dictionary={
        name:bid
  }
    data_dictionary[name]=bid    ##Storing data in dictionary

    value=input("Are there any other bidders: yes or no: ")
    if value=='yes':
        clear_screen()
    else:
        value='no'
highest=0

## Looping Through Dictionary to find Highest

for key in data_dictionary:
    if data_dictionary[key]>highest:
        highest=data_dictionary[key]
        name=key
clear_screen()
print(f"The winner is {name} with bid amount {highest}")


