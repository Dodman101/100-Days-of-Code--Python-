# Don't change the code below
age = input("What is your current age? ")
# Don't change the code above

#Write your code below this line
###################################

##Hint:
#There are 365 days in a year, 52 weeks in a year and 12 months in a year
#Remember to round the results before printing.

#Algorithm
#Calculate the no. of weeks that you have left if you are going to live upto 90
# First get the users age, then subtract it from 90 to get years left
# To get days left, do (years left  * days in a year)
# To get weeks left, do (years left * weeks in a year)
# To get months left, do (years left * months in a year)

# Round off the values and then print the final statement: 

years_left = 90 - int(age)
days_left = round(years_left * 365)
weeks_left = round(years_left * 52)
months_left = round(years_left * 12)

message = f"You have {days_left} days, {weeks_left} weeks and {months_left} months left."

print(message)
