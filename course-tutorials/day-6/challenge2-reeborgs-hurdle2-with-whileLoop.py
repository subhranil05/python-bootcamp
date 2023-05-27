# Hurdle 2
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

## While Loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def full_step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    full_step()
    
    
## For Loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def full_step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for hurdle in range(1,7):
  if not at_goal():  
    full_step()