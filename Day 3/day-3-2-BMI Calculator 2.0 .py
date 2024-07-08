# Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above

#Write your code below this line

##Check the data type
#print(type(height))
#print(type(weight))

##Convert the strings to floats and perform the division
bmi = round(weight / (height ** 2))

#Convert the BMI into an integer and print it 
# print(int(bmi))

if bmi < 18.5 :
    print(f"Your BMI is {bmi} and you are underweight")
elif bmi < 25 :
    print(f"Your BMI is {bmi} and you are normal weight")
elif bmi < 30 :
    print(f"Your BMI is {bmi} and you are overweight")
elif bmi < 35 :
    print(f"Your BMI is {bmi} and you are obese")
else:
    print(f"Your BMI is {bmi} and you are clinically obese")