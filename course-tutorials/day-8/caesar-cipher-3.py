# caesar cipher
# Combine encode and decode function to a new function cesar()
# erduce the lines of code, optimize and better view


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

# process 1
def caesar(input_caesar_text, input_caesar_shift, input_caesar_direction ):
  caesar_text = ""
  for letter in input_caesar_text:
    position = alphabet.index(letter)
    if input_caesar_direction == "encode":
      new_position = position + input_caesar_shift
      caesar_text += alphabet[new_position]
    elif input_caesar_direction == "decode":
      new_position = position - input_caesar_shift
      caesar_text += alphabet[new_position]
  if input_caesar_direction == "encode":
    print(f"The encoded text is {caesar_text}")
  elif input_caesar_direction == "decode":
    print(f"The decoded text is {caesar_text}")

# process 2 [better, mor lines reduced]

def caesar(input_caesar_text, input_caesar_shift, input_caesar_direction ):
  caesar_text = ""
  if input_caesar_direction == "decode":
    input_caesar_shift *= -1
  for letter in input_caesar_text:
    position = alphabet.index(letter)
    new_position = position + input_caesar_shift
    caesar_text += alphabet[new_position]
    
  print(f"The {input_caesar_direction}d text is {caesar_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(input_caesar_text=text, input_caesar_shift=shift, input_caesar_direction=direction)

# separete functions

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, cipher_shift):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - cipher_shift
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}") 
  
  
#   if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
#   elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)