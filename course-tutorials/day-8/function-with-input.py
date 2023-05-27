# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("Hi Rivu")
#   print("How are You?")

# greet()

# function with input

def greet(name):
  print(f"Hi {name}")
  print(f"How are You {name}?")

greet("Subhranil")

# With more than one parameters
# sum of two numbers with function-with-input

def sum_of_numbers(a,b):
  c = a + b
  print(f"Sum is: {c}")

sum_of_numbers(4,5)