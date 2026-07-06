import os
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

## Clearing the Screen

clear_screen()

## Checking Resources Sufficient Function

def resources(user):
    if menu.MENU[user]["ingredients"]["coffee"]>menu.resources["coffee"]:
        print("Sorry there is no enough Coffee!")
        return False
    elif menu.MENU[user]["ingredients"]["water"]>menu.resources["water"]:
        print("Sorry there is no enough Water!")
        return False
    elif menu.MENU[user]["ingredients"]["milk"]>menu.resources["milk"]:
        print("Sorry there is no enough Milk!")
        return False
    else:
        return True 
      
## Start of Program

print("Welcome to the Virtual Coffee Machine☕")
## Importing Menu

import menu
money=0
user=""

## Using While loop to Repeat Menu and ask for Coffee!

while user!="off":
    user=input("What would you like? (espresso/latte/cappuccino): ")
    if user=="off":
        exit(0)
    ## Printing and Evaluating Report

    elif user=="report":
        for item in menu.resources:
            print(f"{item} : {menu.resources[item]}g")
        print(f"Money: ${money}")
    ## Checking user input
    elif user=="latte" or user=="espresso" or user=="cappuccino":
        if resources(user)==True:

            ## Asking coins if Resources Avalaible

            print("Please insert coins.")
            quarters=int(input("How many quarters: "))
            dimes=int(input("How many dimes: "))
            nickles=int(input("How many nickles: "))
            pennies=int(input("How many pennies: "))

            ## Calculating money entered by Customer

            total=(quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)

            ## If money less than cost

            if total<menu.MENU[user]["cost"]:
                print("Sorry there is not enough money. Money Refunded.")
            elif total>=menu.MENU[user]["cost"]:
            
            ## Backing Change if money > costs

                if total>menu.MENU[user]["cost"]:
                    change=total-menu.MENU[user]["cost"]
                    change=round(change,2)
                    print(f"Here is ${change} in change!")

            ## Deducting Resources/ Updating Resources as some are used and also updating Balance/money of MAchine

                money=menu.MENU[user]["cost"]
                menu.resources["water"]=menu.resources["water"]-menu.MENU[user]["ingredients"]["water"]
                menu.resources["water"]=menu.resources["coffee"]-menu.MENU[user]["ingredients"]["coffee"]
                menu.resources["milk"]=menu.resources["milk"]-menu.MENU[user]["ingredients"]["milk"]
            
            ## Giving the Coffee
            
                print(f"Here is your {user}! Enjoy.")



            
        








