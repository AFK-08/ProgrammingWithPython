#*********************Learning Pandas*****************

### Without Pandas Library, we have to do more to manipulate csv files and play with data

## import csv
## with open("./Pandas/weather_data.csv" ,mode="r") as file:
##    data = csv.reader(file)
#### print(temperature)

## Pandas Library make it easy to play with CSV files and 
## much more in Data Analysis and Visualization.

##>> There are 2 Primary Data Structures of Pandas:

######### 1. DataFrame(2 Dimensional- kind of like the whole table)
######### 2. Series(1 Dimensional)- kind of equalant to lists.

## Read API-Reference Pandas to know things you can do with Pandas.

import pandas
data = pandas.read_csv("./Pandas/weather_data.csv")
print(type(data))       
print(data)                  ## It is a DataFrame

####### You can access Columns by these Methods:

print(type(data["temp"]))
print (data["temp"])         ## It is a series dataStructure
# or
print(data.temp)


## You can use different functions provided in library with Series and DataFrames by reading through Documentation.

temprature_list= data["temp"].to_list()
print(temprature_list)

## Prints Average --mean() function:
print(data["temp"].mean())

## Prints Largest in Series
print(data["temp"].max())

###>>>>>>> Get data in  rows

## pull up the row when day is monday
print(data[data.day=="Monday"])

## pull up the row when temp is highest
print(data[data.temp == data.temp.max()])

########Creating DataFrame From Scratch

data_dictionary={
    "names":["Ahmad","Ali","Hamad"],
    "age":[20,19,10]
}
## Converting dictionary into DataFrame.
data = pandas.DataFrame(data_dictionary) 
print(data)


## Looping Through the DataFrames:

students_dictionary = {
    "names": ["Ali","Ahmad","Mahib"],
    "scores": [10,20,30] 
}

student_dataframe = pandas.DataFrame(students_dictionary)
print(student_dataframe)
## Looping:
for (index,row) in student_dataframe.iterrows():
    print(index)

for (index,row) in student_dataframe.iterrows():
    print(row)

print("***************************************")

for (index,row) in student_dataframe.iterrows():
    print(row.scores)




