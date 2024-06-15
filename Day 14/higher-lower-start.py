import random
from art import logo
from game_data import data
from art import vs
from replit import clear

#TODO-2: Import the data from game_data, and randomly select a specific dictionary in the data.
#Create a  function to generate a random item from the list
def random_item():
    """This function fetches a random item from the data list and returns the name, description, country and followers"""
    #Fetch a random dictionary from the data list
    random_dict = random.choice(data)
    name = random_dict['name']
    description = random_dict['description']
    country = random_dict['country']
    followers = random_dict['follower_count']

    return name, description, country, followers


#TODO-8: Repeat step above until the user gets an incorrect answer.
#Use a negated while loop to achieve the game restart effect
end_game = False
user_score = 0

while not end_game:

    # TODO-1: Print the logo
    print(logo)

    #TODO-3: Display the random person and output it in the format Compare A: "name", "description", "country" . 
    #Call the random_item function and make the returned variables available to tbe used
    item_a = random_item()
    print((f"Compare A: {item_a[0]}, {item_a[1]}, {item_a[2]}"))

    #TODO-4: Print the "vs" art
    print(vs)

    #TODO-5: Display the random person and output it in the format Compare B: "name", "description", "country" . 
    #Call the random_item function and make the returned variables available to tbe used
    item_b = random_item()

    #Ensure that compare A is not the same as compare B
    if item_b == item_a:
        item_b = random_item()

    print((f"Compare B: {item_b[0]}, {item_b[1]}, {item_b[2]}"))
        
    #TODO-6: Print the line "Who has more followers? Type 'A' or 'B': " and get input from the user. 
    #Ensure that no matter what case the user inputs, that it will not bring an error.
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    #TODO-7: a)Check the input from the user against the followers and if the user choses the item with the most followers in instagram, add 1 point to the "users_score" 
    followers_a = item_a[-1]
    followers_b = item_b[-1]

    if user_input == 'a' and followers_a > followers_b:
        user_score += 1
        clear()
        print(f"Your current score is: {user_score}")
    elif user_input == 'a' and followers_a < followers_b:
        #End the game by returning true to the negated while loop
        end_game = True
        #If the users choice is incorrect, print out "Sorry, that's wrong. Final score: {users_score}".
        print(f"Sorry, that's wrong. Final score: {user_score}")

    elif user_input == 'b' and followers_b > followers_a:
        user_score += 1
        #If item B wins use it as Compare A
        item_b == item_a
        clear()
        print(f"Your current score is: {user_score}")
    elif user_input == 'b' and followers_b < followers_a:
        #End the game by returning true to the negated while loop
        end_game = True
        #If the users choice is incorrect, print out "Sorry, that's wrong. Final score: {users_score}".
        print(f"Sorry, that's wrong. Final score: {user_score}")

    elif user_input == 'a' and followers_a == followers_b:
        print("Draw. They have an equal number of followers.")

    elif user_input == 'b' and followers_b == followers_a:
        print("Draw. They have an equal number of followers.")

    else:
        print("Invalid user input.")
        #End the game by returning true to the negated while loop
        end_game = True















