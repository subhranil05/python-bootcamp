# Strings: ordered, immutable, text representation

my_string = "Hello World"
multi_line_str = """Hello 
World"""

char = my_string[0]
print(char)

substring = my_string[0:5]
reverse_substr = my_string[::-1] # to reverse the string
print(substring)
print(reverse_substr)

str1 = "Hello"
str2 = "Subhranil"

concat_str = str1 + " " + str2
print(concat_str)

for i in my_string:
    print(i)
    
if 'l' in my_string:
    print("Yes")
else:
    print("No")
    
my_string2 = "   Hello World   "
remove_space = my_string2.strip()  # strip() to remove white space
print(remove_space)

print(my_string.upper())
print(my_string.lower())

print(my_string.startswith('Hello'))
print(my_string.endswith('World'))

print(my_string.find('o'))
print(my_string.count('l'))

print(my_string.replace('World', 'Subhranil'))

# convert each element of string to list element
my_str = "Hey how are you subhranil"
my_list = my_str.split()
print(my_list)

# restore the string from the list
restore_str = ' '.join(my_list)
print(restore_str)

# formatting string

var = "Subhranil"
my_str1 = "The name is %s" % var
print(my_str1)

var = 2
my_str1 = "The number is %d" % var
print(my_str1)

var = 2.2
my_str1 = "The number is %.2f" % var
print(my_str1)


var = "Subhranil"
my_str1 = "The name is {}".format(var)
print(my_str1)

var = 2.2
my_str1 = "The number is {:.2f}".format(var)
print(my_str1)

var = 2.2
var2 = 2
my_str1 = "The float is {:.2f} and the int is {}".format(var, var2)
print(my_str1)

var = "Subhranil"
my_str1 = f"The name is {var}"
print(my_str1)

var = 2.2
var2 = 2
my_str1 = f"The float is {var} and the int is {var2}"
print(my_str1)