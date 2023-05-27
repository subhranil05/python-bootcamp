from art import logo,vs
from game_data import data
from replit import clear
import random

def format_data(rand_dict):
  """Format the random dict into required string"""
  name = rand_dict["name"]
  desc = rand_dict["description"]
  country = rand_dict["country"]
  return f"{name}, a {desc}, from {country}"

def check_follower(data1, data2):
  """compare the follower between two dict"""
  if data1["follower_count"] > data2["follower_count"]:
    return "a"
  else:
    return "b"
def game():
  """Full game steps"""
# Display the art
  print(logo)
  score = 0
  game_continue = True
  
  rand_dict1 = random.choice(data)
  rand_dict2 = random.choice(data)
  # repeat the game
  while game_continue:
    # generate a random dict from data
    rand_dict1 = rand_dict2
    rand_dict2 = random.choice(data)
    while rand_dict1 == rand_dict2:
      rand_dict2 = random.choice(data)
    
    
    print(f"Compare A: {format_data(rand_dict1)}")
    print(vs)
    print(f"Against B: {format_data(rand_dict2)}")
  
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # print(f'A: {rand_dict1["follower_count"]}')
    # print(f'B: {rand_dict2["follower_count"]}')
    clear()
    print(logo)
    if guess == check_follower(rand_dict1, rand_dict2):
      score += 1
      print(f"you are right! Current score: {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      game_continue = False

game()