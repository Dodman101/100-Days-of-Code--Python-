# Don't change the code below
year = int(input("Which year do you want to check? "))
# Don't change the code above

#Write your code below this line

#TODO
#* Check if the year provided is a leap year or not.

#? How To:
#! on every year that is evenly divisible by 4
#!    except every year that is evenly divisible by 100
#!      unless the year is also evenly divisible by 400

#* Layman's language: If the year is evenly divisible by 4 and divisible by 100 and also divisible by 400, it is considered to be a Leap Year.

#*Write an If statement to check if (year % 4 == 0)
#*Write another If statement in the same block to check if (year % 100 != 0)
#*Write another if statement in the same block to check if (year % 400 == 0)
#*Print("Leap Year.")
#*Else print("Not Leap Year")

if (year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
