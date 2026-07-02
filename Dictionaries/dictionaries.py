###Learning about Dictionaries:
programming_dictionary={
    "bug":"Error in the code",
    "Function":"code that can be recalled",
    "loop":"Thing that keeps repeating",
}
print(programming_dictionary["Function"])

##Adding new entry if any//or Editing Existing Entry

programming_dictionary["new"]="This is new entry"
print(programming_dictionary)

##Creating Empty Dictionary
empty_dictionary={}

##Wiping an existing Dictionary
programming_dictionary={}
print(programming_dictionary)

##Looping through the Dictionary
programming_dicts={
    "bug":"Error in the code",
    "Function":"code that can be recalled",
    "loop":"Thing that keeps repeating",
}
for thing in programming_dicts:
    print(thing)            ##It will only print keys not values
    print(programming_dicts[thing]) ##This prints value





