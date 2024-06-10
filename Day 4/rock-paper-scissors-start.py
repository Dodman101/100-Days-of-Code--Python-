import random

rock = '''

    ------
---'  ____)
    (_______)
    (______)
    (_____) 
---._(___)  

'''
paper = '''

    ____
---'  ___)___
        _____)
        ______)
       ______)
---._______)

'''

scissors =  '''

    _____
---'  ___)___
        _____)
      ________)
      (____)
---.__(___)

'''

#TODO: Create a rock paper scissors game, that you can play with the computer.

#!Rules:
#! 1. Rock wins over scissors
#! 2. Paper wins over rock
#! 3. Scissors wins over paper

#* Algorithm
#* Take input from the user and ensure that is converted into an integer
#* Print out the output in ascii form from the users choice. 0 for rock, 1 for paper or 2 for scissors
#* Randomly generate a number from 0 to 2 to indicate what the computer chose and display the appropriate ASCII (Don't forget to import the random function)
#* From the rules, determine if you won that round and print a message out "You lose" , "You Won" or "Its a draw".

game_images = [rock, paper, scissors]

# Human
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#if human_choice == 0:
    #print(rock)
#elif human_choice == 1:
    #print(paper)
#elif human_choice == 2:
    #print(scissors)

#The code below replaces the code above
if (human_choice > (len(game_images) - 1)) or (human_choice < 0):
    print("You typed and invalid number. You lose")
else:
    print(game_images[human_choice])

    #Computer
    print("Computer chose: \n")
    computer_choice = random.randint(0,2)

    #if computer_choice == 0:
        #print(rock)
    #elif computer_choice == 1:
        #print(paper)
    #elif computer_choice == 2:
        #print(scissors)

    #The code below replaces the code above
    print(game_images[computer_choice])

    #Playing Logic
    if (human_choice == 0) and (computer_choice == 2):
        print("You win!")
    elif (human_choice == 2) and (computer_choice == 0):
        print("You win!")
    elif (human_choice == 2) and (computer_choice == 1):
        print("You win!")
    elif (human_choice == computer_choice):
        print("Its a draw")
    else:
        print("You lose")