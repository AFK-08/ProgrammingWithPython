from menu import Menu , MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

import os
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

## Clearing Screen for better Interaction.
clear_screen()

## Constructing Objects from Classes.

money_machine= MoneyMachine()
coffee_maker= CoffeeMaker()
menu=Menu()

## Using While to Keep Running Machine until off

switch=True
while switch==True:
    ## Asking user for drink
    options=menu.get_items()
    choice=input(f"What would you like? {options} : ")

    if choice=="off":
        switch=False

    ### Printing Report
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        ## Finding Drink entered by user
        drink=menu.find_drink(choice)

        ## Checking Sufficient Resources
        if coffee_maker.is_resource_sufficient(drink):
            
            ## Making and Checking Enough Payment
            if money_machine.make_payment(drink.cost):

                ## Offering Coffee
                coffee_maker.make_coffee(drink)

        


