# Design a Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# process 1
password1 = str()
for i in range(0, len(letters)):
  if i <= nr_letters - 1:
    ran_letter = random.randint(0, int(len(letters)) -1)
    password1 += letters[ran_letter] 

password2 = str()
for j in range(0, len(symbols)):
  if j <= nr_symbols - 1:
    ran_symbols = random.randint(0, int(len(symbols)) -1)
    password2 += symbols[ran_symbols]

password3 = str()
for k in range(0, len(numbers)):
  if k <= nr_numbers - 1:
    ran_numbers = random.randint(0, int(len(numbers)) -1)
    password3 += numbers[ran_numbers] 
    
print(f"\n\nyour password is: {password1}{password2}{password3}")


# process 2 [with random.choice] [better one]

password1 = str()
for i in range(0, nr_letters):
    # ran_letter = random.choice(letters)
    password1 += random.choice(letters)

password2 = str()
for j in range(0, nr_symbols):
    # ran_symbols = random.choice(symbols)
    password2 += random.choice(symbols)
    
password3 = str()
for k in range(0, nr_numbers):
    # ran_numbers = random.choice(numbers)
    password3 += random.choice(numbers)
    
print(f"\n\nyour password is: {password1}{password2}{password3}")



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


password_list = []
for i in range(0, nr_letters):
    password_list.append(random.choice(letters))

for j in range(0, nr_symbols):

    password_list.append(random.choice(symbols))

for k in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char
print(f"\n\nyour password is: {password}")