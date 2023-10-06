#### Inheritence ####

from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken=0):
        # create super function to get full access of methods/attributes of parent class
       super().__init__(
          name, price, quantity
        )
       # Run validations against given argumenets
       assert broken >= 0, f"broken {broken} is negetive"
       #Assign to self object
       self.broken = broken