

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
  print("can ride")
  age = int(input("What is your age? "))
  if age < 12:
      bill = 5
      print(f"Child cost is ${bill}")
  elif age <= 18:
      bill = 7
      print(f"Youth cost is ${bill}") 
  else:
      bill = 12
      print(f"Adult cost is ${bill}")
  photo = input("Do you want a photo taken? Y or N? ")
  if photo == "Y":
      bill += 3
  print(f"total bill is ${bill}")
      
else:
  print("can't ride")