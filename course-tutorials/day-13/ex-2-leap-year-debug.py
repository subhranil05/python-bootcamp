year = int(input("Which year do you want to check?"))   ## need to convert the input to 'int' integer as default type of input function is string 'str'

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")