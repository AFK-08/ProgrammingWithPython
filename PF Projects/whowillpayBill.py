#Randomisation and concepts of list used.
#Problem: Friends are at the resturant and everybody puts their bill in the bowl and random card will be selected and he/she will pay the bill.

import random
friends=["Ahmad","Ali","Hassan","Sultan","Sikandar","Usman"]

#Method 1
number=random.randint(0,5)
print(friends[number])

#Method 2
print(random.choice(friends))

