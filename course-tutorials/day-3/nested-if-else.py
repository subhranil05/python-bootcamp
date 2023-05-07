print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("can ride")
  age = int(input("What is your age? "))
  if age < 12:
      print("cost is $5")
  elif age <= 18:
      print("cost is $7") 
  else:
      print("cost is $12")
else:
  print("can't ride")