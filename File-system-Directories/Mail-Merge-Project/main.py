
## Opening File "invited_names.txt" that Contains Names of People for MAIL.
file = open("./File-system-Directories/Mail-Merge-Project/Input/Names/invited_names.txt",    mode="r")

## Stroing Each line/Name of file in a List using readlines()
names_list = file.readlines()
file.close()

## Opening file "starting_letter" to get  Template of MAIL
## Reading it and storing its content in a letter variable
file = open("./File-system-Directories/Mail-Merge-Project/Input/Letters/starting_letter.txt", mode="r")
letter=file.read()
file.close

## For Replacing default [name] in letters to send:
replacing_txt="[name]"

## Looping through list of names,
## Replacing [name] with actual names
## writing letter to new file for each person.

for name in names_list:
    letter = letter.replace(replacing_txt , name.strip("\n"))

    file= open(f"./File-system-Directories/Mail-Merge-Project/ReadyToSend/letter_for_{name.strip("\n")}", mode="w")

    file.write(letter)
    file.close()

## DONE.
print("Mail Merging and Writing Done!")




    