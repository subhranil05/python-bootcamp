# Function with outputs

def sum_of_two():
    result = 5 + 4
    return result

sum_of_two()

# save it to a variable

output = sum_of_two()
print(output)

# Format name function

def format_name(f_name, l_name):
  converted_f_name = f_name.title()
  converted_l_name = l_name.title()

  # print(f"{converted_f_name} {converted_l_name} ")
  return f"{converted_f_name} {converted_l_name}"

output = format_name("sUBhranil", "GhOSh")
print(output)