# Design a Secret Bidding Auction

from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

# Create a function to find the max bidder

def higest_bid(bid):
  max_bid = 0
  for name in bid:
    bid_price = bid[name]
    if bid_price > max_bid:
      max_bid = bid_price
      winner = name
  print(logo)    
  print(f"\n\nCongratulation {winner}, you have won the bid with bid amount of ${max_bid}")

run_again = True  
    
while run_again:
  name = input("What is your name?: ")
  bid_amount = int(input("What's your bid?: $"))
  
  empty_dict = {}
  empty_dict[name] = bid_amount
  
  other_user = input("Are there any other bidders? Type 'yes' or 'no': ")
  if other_user == "no":
    run_again = False
  clear()

higest_bid(bid=empty_dict)