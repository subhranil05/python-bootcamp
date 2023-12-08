# create class called Employee
# Class: A blueprint to create instances
# Instance Variable: Instnace variable contains data that are unque to each instance
# Class variable: Variables that shared upon all instances of a class
class Employee:
    emp_counts = 0 
    hike_amount = 1.05
    # Instance Variable created with constructor
    def __init__(self, first, last, pay) -> None: # Initialize Class attributes
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
    
# Create Class Instances
emp_1 = Employee('Subhranil', 'Ghosh', 60000)
emp_2 = Employee('Test', 'User', 50000)

# Instance Variable: (Manually created)
# emp_1.first = 'Subhranil'
# emp_1.last = 'Ghosh'
# emp_1.email = 'subhranilghosh1212@gmail.com'
# emp_1.pay = 50000

# emp_2.last = 'User'
# emp_2.email = 'testuser1212@gmail.com'
# emp_2.pay = 50000
# emp_2.first = 'Test'

# print(emp_1.fullname())
# print(Employee.fullname(emp_2))
# print(emp_1.pay)
# print(emp_1.apply_hike())
Employee.hike_amount = 1.06   # changing class varaible at class level
emp_1.hike_amount = 2.00  # changing class variable at instance level

print(Employee.hike_amount)
print(emp_1.apply_hike())
print(emp_2.apply_hike())
print(emp_1.__dict__)