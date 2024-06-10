# Don't change the code below
two_digit_number = input("Type a two digit number: ")
# Don't change the code above

###########################################################
#Write your code below this line

##The line below extracts the first digit of the number given
digit_one = two_digit_number[0]
## Extracts the second digit of the number given
digit_two = two_digit_number[1]

## Checks the type
#print(type(digit_one))

##Converts the numbers from string to integer and then adds the two digits together
total = int(digit_one) + int(digit_two)

##Prints the total from the two digits
print(total)