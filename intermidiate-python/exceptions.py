# Error and exceptions
x = -5
if x < 0:
    raise Exception('value of x should be greater than 0')

assert (x>=0), 'x is not +ve'

try:
    a = 5 / 0
except:
    print('an error happened')
    
    
