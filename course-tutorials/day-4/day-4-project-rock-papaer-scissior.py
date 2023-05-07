# Build a Rock, Scissior and Paper Game

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Process 1

import random
answer = int(input("What do you choose? Type '0' for Rock, '1' for Paper or 2 for Scissior: "))
if answer < 3 or answer >= 0:
    if answer == 0:
        print(rock)
    elif answer == 1:
        print(paper)
    else:
        print(scissors)

    computer = random.randint(0,2)
    
    if computer == 0:
        print(f"Computer choose\n\n{rock}")
    elif computer == 1:
        print(f"Computer choose\n\n{paper}")
    elif answer > 2:
        print("")
    else:
        print(f"Computer choose\n\n{scissors}")

    if answer == 0 and computer == 1:
        print("\n\nYou Loose")
    elif answer == 1 and computer == 2:
        print("\n\nYou Loose")
    elif answer == 2 and computer == 0:
        print("\n\nYou Loose")
    elif answer == computer:
        print("\n\nMatch Draw")
    else:
        print("\n\n@@@@@@ YOU WON @@@@@@")
else:
  print("\nPlease selcet valid option")
  
  

# Process 2 [with list]

import random
answer = int(input("What do you choose? Type '0' for Rock, '1' for Paper or 2 for Scissior: "))
if answer < 3 and answer >= 0:
    game_images = [rock, paper, scissors]
    print(game_images[answer])

    computer = random.randint(0,2)
    
    print("Computer choose:\n")
    print(game_images[computer])

    if answer == 0 and computer == 1:
        print("\n\nYou Loose")
    elif answer == 1 and computer == 2:
        print("\n\nYou Loose")
    elif answer == 2 and computer == 0:
        print("\n\nYou Loose")
    elif answer == computer:
        print("\n\nMatch Draw")
    else:
        print("\n\n@@@@@@ YOU WON @@@@@@")
else:
  print("\nPlease selcet valid option")