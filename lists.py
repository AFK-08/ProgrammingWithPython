#list is used to store multiples values and they have a relationship between them and where order is important
numbers=[1,2,3,4,5,4]
print(numbers[2])
names=["Ahmad","Ali","Hassan"]
print(names[1])


numbers[2]=7            #you can change any position value of list
print(numbers)

numbers.remove(4)       #remove the first one value equal to value
print(numbers)


names.append("Iqrar")   #It can add items to list at the end
print(names)