print("Welcome to the Treasure Island.\nYour Mission is to find Treasure\n")
choice=input("    Type 'left' or 'right'\n")
if choice=="left":
    choice2=input("Want to swim or wait\n")
    if choice2=="wait":
        choice3=input("Which door red , yellow, blue\n")
        if choice3=="yellow":
           print("You win")
        elif(choice3=="red"):
           print("burned by fire. Game over")
        else:
            print("Game Over. Eaten by Lion")
    else:
        print("Attacked by Trout. Game over.")
else:
    print("Fall into Mud. Game over.")
