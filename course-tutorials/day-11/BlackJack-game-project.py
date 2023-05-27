############### Blackjack Project #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

############### Our Blackjack House Rules #####################


from art import logo
import random
from replit import clear

# Create a deal_card() function that uses the List below to *return* a random card. #11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  """Return a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card


def calculate_score(cards):
  """This function going to calulate sum of user's and computer's card and return the score"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
      cards.remove(11)
      cards.append(1)
  return sum(cards)  

  #Create a function called calculate_score() that takes a List of cards as input 
  #and returns the score. 
  #Look up the sum() function to help you do this.

def compare(user_score, computer_score):
  """This function is going to comapare both scores and find the winner"""
    
  if user_score == computer_score:
    return "Its a Draw"
  elif  computer_score == 0:
    return "You Loose!! Computer has a Blackjack"  
  elif user_score == 0:
    return "Hurray, You have a Blackjack, You Win "
  elif user_score > 21:
    return "You went over, you loose!!"
  elif computer_score > 21:
    return "You Won, Conmputer has went over"
  elif user_score > computer_score:
    return "You Won"
  else:
    return "You loose!!"


def play_game():
  """This function will keep the whole game running"""
  print(logo)
  
#Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

  user_cards = []
  computer_cards = []
  game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

#The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"user's cards are {user_cards}, current score is {user_score}")
    print(f"computer's first card is {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      
      #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      deal_again = input("Type 'y' to get another card, type 'n' to pass: ")
      if deal_again == "y":
        user_cards.append(deal_card())
      elif deal_again == "n":
        game_over = True
        
#Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  
  print(compare(user_score, computer_score))
  print(f"computer chose {computer_cards}")

#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
  clear()
  play_game()
