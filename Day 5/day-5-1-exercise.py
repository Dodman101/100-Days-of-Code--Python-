# Don't change the code below
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# Don't change the code above

#Write your code below this row

#TODO: This program should calculate the average student height from a list of heights.

#? Hint
#? To calculate the average, you need to sum the heights then divide them by the lenght of the list of heights.

#! Rules
#! Do not use the "len()" function or the "sum()" function.
#! Find a way of summing the heights and getting the len by using for loops.

#*Algorithm
#* Use for loops to find the sum of the student heights. 
#* Use for loops to find the len of the student heights so that we can calculate the average later.
#* Calcuate the average
#* Round it off to the nearest whole number and print it out.

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)