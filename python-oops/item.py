import csv

# creating class
# creating own data types
class Item:
    #class atrribute
    pay_rate = 0.8 # discounted rate
    all_product = []
    # create constructor
    def __init__(self, name: str, price: float, quantity=0):
       # Run validations against given argumenets
       assert price >= 0, f"price {price} is negetive"
       assert quantity >= 0, f"quantity {quantity} is negetive"
       
       #Assign to self object
       self.__name = name
       self.price = price
       self.quantity = quantity
       
       Item.all_product.append(self)
     # set this decorator to keep readonly attribute
    @property
    def name(self):
        return self.__name
    
    #to set new value to read only 'name' attribute
    @name.setter
    def name(self, value):
        # restrict the lenght of name
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value
    # define function inside classes are called methods
    def calulate_total_price(self):
    #   return a * b
        return self.price * self.quantity
    
    def apply_discount(self):
        #accessing class attribute 'pay_rate'
        self.price = self.price * self.pay_rate
    
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}' )"
    
    # creating decoretors (class method())
    @classmethod
    def instance_pullfrom_csv(cls):
        with open('python-oops/items.csv', 'r') as data:    #reading/loading data from .csv file
            reader = csv.DictReader(data)
            items = list(reader)
        for item in items:
            # print(item)
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = float(item.get('quantity'))
            )   
    # Create static method
    @staticmethod
    def is_integer(num):
        # will count out the floats that are point zero
        # for i.e: 10.0, 12.0, 15.0
        if isinstance(num, float):
            #count floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"