## Nested Lists and Dictionaries:

##           Simple dictionary is like this:
##           dictionary={key1:value, key2:value}

##           Nested list and dictionary:
##           dictionary={key1:[list], key2={dictionary}}

            ##A nested dictionary can have a dictionary or list as a value of its key

capitals={
    "France":"Paris",
    "Germany":"Berlin",           ##simple dictionary
    "Pakistan":"Islamabad",  
}
for key in capitals:
    print(key)
    print(capitals[key])
    print("**********")

##Lists inside dictionary

travel_log={
    "Germany":"Berlin",            
    "Pakistan":["Murree","Lodhran","Lahore"],
}
print(travel_log["Pakistan"][1])   ##Access element in lists

for key in travel_log:
    print(key)
    print(travel_log[key])
print("**********")

nested_list=["A","B",["C","D"]]  ## List inside list

print(nested_list[2][1])       ##Access element inside nested list.
print("************")

## Dictionary Inside dictionary and lists
## Complex Nesting- try to understand single line

travel_log={
      
        "Germany":{
        "Total_visits":12,
        "cities":["Paris","Dijin","lille"],
      },
     "Pakistan":{
         "Total_visits":12,
         "cities":["Murree","Lodhran","Lahore"],
     }   
}
print(travel_log["Pakistan"]["cities"][2])  ##PRINTING LAHORE


