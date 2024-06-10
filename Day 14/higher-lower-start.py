import random
from replit import clear

# TODO-1: Import the logo
from art import logo
print(logo)

#TODO-2: Import the data from game_data, and randomly select a specific dictionary in the data.
from game_data import data

def choice_a():
    """This function is supposed to select and output a random celebritys' name, description and country"""
    random_index = random.randint(0,len(data)-1)

    random_list_item = data[random_index]

    name = random_list_item['name']
    followers_a = random_list_item['follower_count']
    description = random_list_item['description']
    country = random_list_item['country']

    print(f"Compare A: {name}, {description}, {country}")

    return followers_a
    
def choice_b():
    """This function is supposed to select and output a random celebritys' name, description and country"""
    random_index = random.randint(0,len(data)-1)

    random_list_item = data[random_index]

    name = random_list_item['name']
    followers_b = random_list_item['follower_count']
    description = random_list_item['description']
    country = random_list_item['country']

    print(f"Compare B: {name}, {description}, {country}")

    return followers_b


#TODO-3: Display the output of the generated dictionary in the format Compare A: "name", "description", "country" . 
followers_a = choice_a()
print(followers_a)

#TODO-4: Import and print the "vs" art
from art import vs
print(vs)

#TODO-5: Display the output of the generated dictionary in the format Compare B: "name", "description", "country" . 
followers_b = choice_b()
print(followers_b)

#TODO-6: Print "Who has more followers? Type 'A' or 'B': " and get input from the user. 
users_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

#TODO-7: a)Check the input from the user and if during the comparison, the user choses the celebrity with the most followers in instagram, add 1 point to the "users_score" and use the celebrity as "Compare A" and generate another random dictionary and display it as "Compare B". b)Else if the users choice is incorrect, print out "Sorry, that's wrong. Final score: {users_score}" and end the game there.

FOLLOWER_A = followers_a
FOLLOWER_B = followers_b
users_score = 0

def check_a():
    if FOLLOWER_A > FOLLOWER_B:
        print("You get an extra score")
        # users_score += 1
        B = choice_b()
        print(B)


def check_b():
    if FOLLOWER_B > FOLLOWER_A :
        print("You get an extra score")
        # users_score += 1
        A = choice_a()
        print(A)


#TODO-8: Repeat step 7a until the user gets an incorrect answer.
end_game = False

while not end_game:
    if users_choice == 'A':
        check_a()
        users_score += 1
        end_game = True 
        print(F"Final score: {users_score}")

    elif users_choice == 'B':
        check_b() 
        users_score += 1
        end_game = True  
        print(F"Final score: {users_score}")    

    elif FOLLOWER_A == FOLLOWER_B:
        print("You got it, continue playing")
        users_score += 1
        print(F"Final score: {users_score}")
    else:
        print("Invalid input try again!")
        end_game = True
        print(F"Sorry, that's wrong. Final score: {users_score}")





