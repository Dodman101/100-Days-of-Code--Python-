# Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# Don't change the code above

#Write your code below this line

##Check the data type
print(type(height))
print(type(weight))

##Convert the strings to floats and perform the division
bmi = float(weight) / float(height) ** 2

#Convert the BMI into an integer and print it 
print(int(bmi))