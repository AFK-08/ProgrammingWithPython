import pandas
import os
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

clear_screen()

data = pandas.read_csv("./NATO-Alphabets Project/nato_phonetic_alphabet.csv")

code_dictionary = {row.letter:row.code for (index,row) in data.iterrows()}

user_name = input("Enter your name: ")

code_list = [code_dictionary[letter.upper()] for letter in user_name]

print(code_list)







