import random

#TODO-1: Welcome the user to the game.
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#TODO-2: Create a list with the numbers from 1 to 100 and a variable called "correct_score" that is going to hold a random number between 1 and 100
numbers = []
for number in range(1,101):
    numbers.append(number)

# print(numbers)
correct_score = random.choice(numbers)
print(correct_score)

END_GAME = False

#TODO-3: Create two variables "easy" and "hard" which will display 10 and 5 attempts respectively once the user types any of them and stores the attempts in a variable called "attempts". 
game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if game_level == "easy":
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
elif game_level == "hard":
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
else:
    print("Invalid input. Please try again!")

#TODO-4: Ask the user to guess a number
users_guess = int(input("Make a guess: "))

#TODO-5: Create a function called "check_guess" that will check to see if the user's guess is correct. If the guess greater that the correct guess, print "Too high" or "Too low" if the user's guess is less than the correct score or if the user's guess is correct print "You got it. The correct number is {correct_score}" and end the game. 
# def check_guess():
#     if users_guess > correct_score:
#         print("Too high.")
#     elif users_guess < correct_score:
#         print("Too low.")
#     elif users_guess == correct_score:
#         return users_guess

#TODO-7: While the users guess is not correct, ask the user to guess again and continue reducing his attempts until they either get it right or run out of attempts ending the game. 
while not END_GAME:

    # check_guess()
    if users_guess > correct_score:
        print("Too high.")
    elif users_guess < correct_score:
        print("Too low.")
    elif users_guess == correct_score:
        print(f"You got it. The answer was {correct_score}")
        END_GAME = True

    #TODO-6: If the user guesses incorrectly, ask them to guess again and minus  1 attempt from the attempts variable.
    if users_guess > correct_score or users_guess < correct_score:
        print("Guess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
        if attempts == 0:
            print("You've run out of attempts!")
            END_GAME = True
        else:
            users_guess = int(input("Make a guess: "))
    

