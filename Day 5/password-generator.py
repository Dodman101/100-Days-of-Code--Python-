#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


#TODO: Write a program to generate a random password for the user according to their input.

#! Do the Easy level first, where they follow each other according to the prompt order.
#! Do the Hard level, where the generated password is also completely random. 

#* Algorithm
#* Pick nr_letters randomly from the list of letters use the random function. 
#* Pick nr_symbols randomly from the list of symbols using the random function. 
#* Pick nr_numbers randomly fro the list of number use the random function. 
#* Concantenate the letters to the symbols then to the numbers
#* Once this is done, see how you can now make them random. 

# Randomly generate x numbers from the len of the letters
#random_index = random.randint(0, len(letters))

#The length of the list of random indexes is supposed to be the same as the user input 
#nr_letters
#random_indexes = []

#for index in random_indexes:
    #if nr_letters == random_indexes:
        #random_indexes.append(index)
#print(random_indexes)

#if (len(random_indexes_list) != nr_letters):
    #for index in letters:
        #print(index)
        #random_indexes_list.append(index)
    #print(random_indexes_list)
#else:
    #print("Didn't work")

# create an empty list
# letter_list = []

# # add the list of values from 0 to nr_letters
# for n in range(0, nr_letters):
#     letter_list.append(n)
    
# print(letter_list)

# # Transform the list by replacing the indexes with a letter in the letters list and create a new list. 

# individual_letters = []

# for l in letter_list:
#     individual_letter = letters[l]
#     individual_letters.append(individual_letter)
# print(individual_letters)

# # Concatenate the strings together
# password_string = str()
# for i in individual_letters:
#     password_string += i
# print(password_string)

# print(random.choices(password_string))

#? The Solution

#Easy Level
# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

#Hard Level

password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list:
    password += char

print(password)