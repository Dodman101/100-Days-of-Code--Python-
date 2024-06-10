# Tip Calculator Project

#TODO: 
##*First print the welcome message
##*Get the bill amount from the user
##*Get the tip percentage from the user
##*Get the number of people splitting the bill

##*Convert the percentage into float format
##*ultiply it by the total bill to get the total tip amount
##*Add the total tip to the bill
##*Divide the sum of the total tip and total bill by the number of people sharing
##*Display the output to the user.

##! Note: Money is always represented in two decimal places. 
##! Also note that all inputs will always have a (str) type, so remember to perform type conversions on them where necessary.

#?Use (*-green,?-blue,!-red, TODO-purple/orange) for formatting



print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give ? 10 ,12, or 15? ")
people = input("How many people to split the bill ? ")

percentage_tip = int(tip) / 100
tip_amount = round(float(bill) * percentage_tip ,2)
final_bill = round(float(bill) + tip_amount,2)
bill_per_person = round(final_bill / int(people),2)
final_amount = "{:.2f}".format(bill_per_person)

message = f"Each person should pay: ${final_amount}"

print(message)

