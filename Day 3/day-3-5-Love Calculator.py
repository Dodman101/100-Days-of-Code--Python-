# Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

#Write your code below this line
#TODO: "Take both people's names and check for the number of times the letter in the word TRUE occurs. Then check the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number."

#? Conditions:
#? If the score is less than 10 or greater than 90, the message should be: "Your score is x, you go together like coke and mentos."
#? If Love score between 40 and 50, the message should be: "Your score is y, you are alright together"
#? Else print("Your score is z.")

#! Note: 
#! Use the lower() function to change the names to lowercase
#! Use the count() function to count the number of occurrences of a letter

#* How to:
#* Concatenate the two names into one name. "combined_names"
#* Use this to change the case of the name into lowercase "combined_names_lower = combined_names.lower()"
#* Count the occurences of the word TRUE first "T = combined_names_lower.count("t")" do this for all the characters in the word TRUE.
#* Sum up the occurrences of TRUE
#* Do the same to the word LOVE
#* Convert the sums of the two words into a string and then concatenate the two sums to provide the score.
#* Check against the conditions and remember to use logical operators (AND, OR, and NOT) where necessary.
#* Then display a message to the user.

combined_names = name1 + name2
combined_names_lower = combined_names.lower()

# Checking occurrences in the word TRUE
T = combined_names_lower.count("t")
R = combined_names_lower.count("r")
U = combined_names_lower.count("u")
E = combined_names_lower.count("e")

sum_of_true = T + R + U + E

# Checking occurrences in the word LOVE
L = combined_names_lower.count("l")
O = combined_names_lower.count("o")
V = combined_names_lower.count("v")
E = combined_names_lower.count("e")

sum_of_love = L + O + V + E

# Calculating the score
score = str(sum_of_true) + str(sum_of_love)
score_as_int = int(score)

if (score_as_int <= 10) or (score_as_int > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score_as_int >= 40) and (score_as_int <= 50):
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")


