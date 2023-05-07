# tip calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
total_bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give 10, 12, or 15? "))
people = int(input("how many people to split the bill? "))
final_tip = tip / 100 * total_bill
final_bill = final_tip + total_bill
pay = final_bill / people
# final_pay = round(pay, 2)
final_pay = "{:.2f}".format(pay)   #-- advance formatting incase of only 1 digit after decimal
print(f"each person should pay: ${final_pay}")