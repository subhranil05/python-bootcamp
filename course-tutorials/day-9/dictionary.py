programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
}

# retrive element from dictionary

print(programming_dictionary["Bug"])

# add item to dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

# create empty dictionary

empty_dict = {}

# wipe the entire dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# edit an item in dictionary

programming_dictionary["Bug"] = "only insects"
print(programming_dictionary)

# loop through dictionary

for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])