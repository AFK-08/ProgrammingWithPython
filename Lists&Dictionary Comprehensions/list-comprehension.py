
## Lists Comprehension- Easy to manipulate and create lists.
numbers = [1,2,3]
## Suppose we want to create new list from this by adding 1 to each item in the numbers list.

## Traditional Way:
"""
    new_list=[]
    for n in numbers:
        n = n+1
        new_list.append(n)
"""
## But with list Comprehension:
## new_list = [new item for item in list]

new_list= [n+1 for n in numbers]
print(new_list)

## Some other stuff:

name = "Ahmad"
letters_list = [letter for letter in name]
print(letters_list)


range_list = [n*2 for n in range(1,6)]
print(range_list)

## Conditional List Comprehension:

words =["hard","core","ultra","impediment","action","take"]
short_words = [word for word in words if len(word)<5]
print(short_words)

large_words = [word.upper() for word in words if len(word)>5]
print(large_words)




