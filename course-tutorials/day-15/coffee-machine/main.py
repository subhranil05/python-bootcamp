from data import MENU, logo, resources
print(logo)
# TODO Prompt user by asking What would you like? (espresso/latte/cappuccino):
user_input = input("What would you like? (espresso/latte/cappuccino):")

def report():
    Water = resources["water"]
    Milk = resources["milk"]
    Coffee = resources["coffee"]
    print(f"Water: {Water}")
    print(f"Milk: {Milk}")
    print(f"Coffee: {Coffee}")
report()

