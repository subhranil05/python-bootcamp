# Design a Simple Calulator tool

from art import logo

print(logo)

#function for add
def add_of_two(a, b):
  """This function will add two numbers"""
  return a + b


def subs(a, b):
  """This function will substract two numbers"""
  return a - b

def multi(a, b):
  """This function will multiply two numbers"""
  return a * b

def divide(a, b):
  """This function will divide two numbers"""
  return a / b

operations = {"+": add_of_two,
              "-": subs,
              "*": multi,
              "/": divide
             } 

def calculator():
  """recursion function to start a new calculator as user input"""
  num1 = float(input("Type your first number: "))
  should_continue = True
  
  while should_continue:
    for key in operations:
      print(key)
    
    sign = input("Pick your operation symbol line above: ")
    num2 = float(input("Type your next number: "))
    
    calculation = operations[sign]
    answer = calculation(num1, num2)
    
    print(f"Your answer: {num1} {sign} {num2} = {answer}")
    
    if input(f"Type 'y' to calculating with {answer} or 'n' to start a new: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()