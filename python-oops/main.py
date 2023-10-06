from item import Item
from phone import Phone
# create instances using the class
item1 = Item("phone", 200, 10)
item2 = Item("computer", 1000, 15)
item3 = Item("headphones", 50, 20)
item4 = Item("charger", 30, 12)
item5 = Item("watches", 60, 12)

# Item.instance_pullfrom_csv()
# print(Item.all_product)

# print(Item.is_integer(7.0))
# create attributes

# item1.name = "phone"
# item1.price = 100
# item1.quantity = 10

#calling the method
# item1.calulate_total_price(item1.price, item1.quantity)
# print(item1.calulate_total_price(item1.price, item1.quantity))

# item2.name = "computer"
# item2.price = 1000
# item2.quantity = 15

# You can alway add extra attributes which not present in constructor
# item2.has_numPad = False

# print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)
# print(item1.quantity)
# print(item2.quantity)
# print(item1.calulate_total_price(item2.price, item2.quantity))

# print(item1.calulate_total_price())
# print(item2.calulate_total_price())
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

#magic attributes
# print(Item.__dict__)  ## Print all class level attributes
# print(item1.__dict__) ## print all instance level attributes

# item1.apply_discount()
# print(item1.price)

# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# print(Item.all_product)

# Print the product's name only from the list
# for instance in Item.all_product:
#     print(instance.name)

phone1 = Phone("Oneplus", 200, 4, 1)
# phone1.broken = 1
phone2 = Phone("Samsung", 300, 5, 2)
# phone2.broken = 2
# print(phone1.calulate_total_price())
# print(Item.all_product)

#### Encapsulasion ####

# print(item1.name)

item1.name = "editedcihfciakcnfe"

print(item1.name)