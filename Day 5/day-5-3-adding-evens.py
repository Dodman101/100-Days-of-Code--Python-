#Write your code below this line

#TODO: Write a program that calculates the sum of all of the even numbers from 1 to 100 including 1 and 100

#! Important
#! There should only be one print statement in your console output. It should just print the final total and not every step of the calculation.

#? Hint
#? Use the "range()" function.

#* Algorithm
#* Declare a variable even_numbers with the value of 0
#* Use a for loop to loop between the numbers from 2 to 100, use a step of 2 to get the even numbers in this range. for number in range(2,101,2)
#* Alternatively, you could use the modulo function to check if the result is divisible by 2. If yes add the numbers that are divisible by 2. Use an if statement to check this.
#* Perform the summation of the list of even numbers
#* Print out the results. 

even_numbers = 0
for number in range(2,101,2):
    even_numbers += number
print(even_numbers)
