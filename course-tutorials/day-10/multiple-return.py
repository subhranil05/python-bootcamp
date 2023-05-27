def format_name(f_name, l_name):
  if f_name == "" and l_name == "":
    return "Your inputs are empty!!"
  converted_f_name = f_name.title()
  converted_l_name = l_name.title()

  # print(f"{converted_f_name} {converted_l_name} ")
  return f"{converted_f_name} {converted_l_name}"

output = format_name(input("Write you first name here: "), input("Write you last name here: "))
print(output)