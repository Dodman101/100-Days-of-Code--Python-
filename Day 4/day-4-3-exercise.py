# Don't change the code below
row1 = ["⬛", "⬛", "⬛"]
row2 = ["⬛", "⬛", "⬛"]
row3 = ["⬛", "⬛", "⬛"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \n")
# Don't change the code above

#Write your code below this line

#TODO: The program should allow you to enter the position of the treasure using a two digit system. The first digit is the horizontal column number and the second digit is the vertical row number. Then mark the spot with an X.

#*Algorithm
#* Interpret the input from the user and split the two digits.
#* Assign the first digit to the column and the second digit to the row
#* Use the row digit to fetch the specific row from the rows provided
#* Use the column digit to append the X to the fetched row
#* Print the map

column = int(position[0])
row = int(position[1])

#My solution
#if row == 1:
    #row1[column - 1] = "X"
    #print(f"{row1}\n{row2}\n{row3}")
#elif row == 2:
    #row2[column - 1] = "X"
    #print(f"{row1}\n{row2}\n{row3}")
#elif row == 3:
    #row3[column - 1] = "X"
    #print(f"{row1}\n{row2}\n{row3}")

#The solution
selected_row = map[row - 1]
selected_row[column - 1] = "X"

#Write your code above this row

# Don't change rhe code below
print(f"{row1}\n{row2}\n{row3}")
