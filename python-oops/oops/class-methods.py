# regular methods: regular methods in a class automatically takes the instance as first arguments
# class methods: class methods in a class automatically takes the class as first arguments
# static method: static methods don't pass anything automatically as first argument. These are just like normal function

class Employee:
    emp_counts = 0 
    hike_amount = 1.05
    # Instance Variable created with constructor
    def __init__(self, first, last, pay): # Initialize Class attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last  + '@gmail.com'
        Employee.emp_counts += 1
        
    # Create Method    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_hike(self):
        self.pay = int(self.pay * self.hike_amount)
        return self.pay
    
    # creating class method with decorator 'classmethod'
    @classmethod
    def set_hike_amt(cls, amt):
        cls.hike_amount = amt
        
    # Alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
# Create Class Instances
emp_1 = Employee('Subhranil', 'Ghosh', 60000)
emp_2 = Employee('Test', 'User', 50000)

emp_str_1 = 'Ravi-Gupta-10000'
emp_str_2 = 'Jack-Ryder-5000'

first, last, pay = emp_str_1.split('-')

# emp_3 = Employee(first, last, pay)
emp_3 = Employee.from_string('Ravi-Gupta-10000')
emp_4 = Employee.from_string('Jack-Ryder-5000')
Employee.set_hike_amt(1.06)  # using class method to modify hike amount


print(Employee.hike_amount)
print(emp_1.hike_amount)
print(emp_2.hike_amount)
print(emp_3.first, emp_3.last, emp_3.email)
print(emp_4.first, emp_4.last, emp_4.email)