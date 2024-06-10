import random

# Split string method
names_string = input("Give me everybody's names, separared by a comma. \n")
names = names_string.split(", ")
# Don't change the code above

#Write your code below this line

#TODO: Create a program that picks a name randomly from the list and appends it to a sentence and outputs the message to the user.

#! Hint
#! Use the len() function.

#* Algorithm
#* Choose a name from the list by finding the len of the list, which will be used later in randomisation
#* Then introduce the random function to make the choosing random, choose_a_name = random.randint(0,lenght of the list)
#* Fetch the name from the list from the random integer generated. random_name = names(choose_a_name)
#* Append the choosen name to a string "...is going to buy the meal today!"
#* Print the message to the user.

name_list = len(names)

choose_a_name = random.randint(0, name_list - 1)

random_name = names[choose_a_name]

print(f"{random_name} is going to buy the meal today!\n")