#Write your code below this line

#TODO: Write a program to automatically print the solution to the FizzBuzz game

#! Rules
#! 1. Your program should print each number from 1 to 100 in turn.
#! 2. When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#! 3. When the number is divisible by 5 then instead of printing the number it should print "Buzz".
#! 4. And if the number is divisible by both 3 and 5 e.g 15 then instead of the number it should print "FizzBuzz"

#* Algorithm
#* Declare a variable number_list which equals to the range 1 to 101 in order for it to include 1 and 100
#* Use an if function in the for loop to check if a number is divisible by 3 by using the modulo function and if true, it should print "Fizz"
#* Use an elif after the first if function to check if a number is divisible by 5 by also using the modulo funciton and if true, it should print "Buzz"
#* Add another elif function to check for numbers that are divisible by 3 and 5 and if true, it should print "FizzBuzz"
#* Print the numbers inside the for loop.

number_list = range(1,101)
for number in number_list:
    if (number % 3 == 0) and (number % 5 == 0):
        number = "FizzBuzz"
    elif (number % 3 == 0):
        number = "Fizz"
    elif (number % 5 == 0):
        number = "Buzz"
    print(number)
