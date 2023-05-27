################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")



# Local scope

def num_print():
  a = 1
  print(f"number is {a} ")

num_print()
print(f"number is {a} ")  ## will not work as 'a' is inside function scope, so 'a' defined as Local scope variable

# Global scope

a = 1

def num_print():
  print(f"number is {a} ")

num_print()
print(f"number is {a} ") ## This will work as 'a' is defined outside of function scope, so 'a' defined as Global scope variable



# Modify global scope variable

# It is not recomended to modify Global varible inside a function or local scope
enemies = 1
def increase_enemies():
  # global enemies
  return enemies + 1
  print(f"enemies inside function: {enemies}")

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


# Global constants
# Alway put variable name in upper case

PI = 3.14
URL = "https://youtube.com"
ID  = "SUBH001"

def global_cons():
  PI