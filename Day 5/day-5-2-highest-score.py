# Don't change the score below
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# Don't change the code above

#Write your code below this row

#TODO: Write a program to get the highest score from a list of scores.

#!Rules
#! Do not use the "max()" function.

#* Algorithm
#* Loop though the list and check for the highest value
#* Print it.

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")