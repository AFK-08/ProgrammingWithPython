import random
## Dictionary Comprehensions:
## dictionary = {newKey:newValue for item in PythonSequence if test}
## Some Practical Stuff:

students = ["Ahmad","Mahib","Abdul","Saif","Usman"]
student_score = {student:random.randint(1,100) for student in students}

print(student_score)

## Creating new dictionary by modifying previous one:

## new_dict = {newKey:newValue for (key,value) in dict.item() if test}

passed_students = {student:score for (student,score) in student_score.items() if score>50}

print(passed_students)
