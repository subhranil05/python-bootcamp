# Design a Simple Calulator tool

from art import logo

print(logo)

#function for add
def add_of_two(a, b):
  """This function will add two numbers"""
  return a + b

#function for substract
def subs(a, b):
  """This function will substract two numbers"""
  return a - b

#function for multiply
def multi(a, b):
  """This function will multiply two numbers"""
  return a * b

#function for divide
def divide(a, b):
  """This function will divide two numbers"""
  return a / b

operations = {"+": add_of_two,
              "-": subs,
              "*": multi,
              "/": divide
             } 

num1 = int(input("Type your first number: "))

for key in operations:
  print(key)

sign = input("Pick your operation symbol line above: ")
num2 = int(input("Type your second number: "))

calculation = operations[sign]
answer = calculation(num1, num2)

print(f"Your answer: {num1} {sign} {num2} = {answer}")