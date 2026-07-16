## Reading from the file

file = open("my_file.txt")  ## opening file and assigning to variable
data = file.read()          ## reading file and assigning contents
print( data )
file.close()                ## closing file


## By using with open you donot need to close files.
with open("my_file.txt") as file:
    data = file.read()         
    print( data )

## Writing to the files:
## mode "w" will write but delete the old text but if you want to add
## keeping previous text then,,,,,,mode= "a" which is append.

with open("my_file.txt", mode="a") as file:
    file.write("I am justing.. \n")


