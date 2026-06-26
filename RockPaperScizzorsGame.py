import random

#Game Menu

print("Welcome to the Game")
choice=int(input("Enter your choice: \n Type 0 for Rock\n Type 1 for paper\n Type 2 for scizzors\n"))

if(choice<0 or  choice>2):
  print("Invalid Input. Play the Game Again")  #Input Validation
  exit(0)
  

choicelist=[0,1,2]                      #Randomisation
ComputerTurn=random.choice(choicelist)

#Computer Turns

if ComputerTurn==0:
 print("Computer chooses Rock")
elif ComputerTurn==1:
 print("Computer chooses Paper")
elif ComputerTurn==2:
 print("Computer chooses Scizzors")

#Evaluation based on rules

if choice==ComputerTurn:
    print("It's a draw. Play Again")
elif ComputerTurn==0:
    if choice==1:
     print("you Win. Paper covers the Rock")
    else:
     print("Computer Wins. Rock smashes Scizzors")
elif ComputerTurn==1:
    if choice==0:
     print("Computer Win. Paper covers the Rock")
    else:
     print("You Win. Scizzors cuts Paper")
elif ComputerTurn==2:
    if choice==0:
     print("You Win. Rock smashes Scizzors")
    else:
     print("Computer Wins. Scizzors cuts Paper")



