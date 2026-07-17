#list is used to store multiples values and they have a relationship between them and where order is important
numbers=[1,2,3,4,5,4]
print(numbers[2])
names=["Ahmad","Ali","Hassan"]
print(len(numbers))
print(names[1])



numbers[2]=7            #you can change any position value of list
print(numbers)

numbers.remove(4)       #remove the first one value equal to value
print(numbers)


names.append("Iqrar")   #It can add items to list at the end
print(names)

#Nested Lists 

Q1=[1,2,3,4,5]
Q2=[6,7,8,9]
sum=[Q1,Q2]
print(sum)
print(sum[0][0])
print(sum[1][1])
print(sum[0])
print(sum[1])