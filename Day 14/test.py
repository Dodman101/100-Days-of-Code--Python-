# # TODO
# 1. Pick a random person from game_data

import random
from game_data import data


def random_person():
    personality = random.choice(data)
    name = personality['name']
    description = personality['description']
    country = personality['country']
    followers = personality['follower_count']

    # print(f"Compare A: {name}, {description}, {country}")
    return followers, personality, name, description, country


from art import logo
print(logo)


# Random person 1 picked
followers, personality, name, description, country = random_person() 
followers_a = followers
personality_a = personality
print(followers)
# print(personality)
print(f"Compare A: {name}, {description}, {country}")

from art import vs
print(vs)

# Random person 2 picked
followers, personality, name, description, country = random_person() 
followers_b = followers
personality_b = personality
print(followers)
# print(personality)
print(f"Compare B: {name}, {description}, {country}")

users_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
users_score = 0

if users_choice == 'A' and followers_a > followers_b:
    # followers_check()
    users_score += 1
    retain_personality = personality_a
    print(retain_personality)
    print(f"{users_score}")
elif users_choice == 'A' and followers_a < followers_b:
    # followers_check()
    print(f"{users_score}")
elif users_choice == 'B' and followers_b > followers_a:
    # followers_check()
    users_score += 1
    retain_personality = personality_b
    print(retain_personality)
    print(f"{users_score}")
elif users_choice == 'B' and followers_b < followers_a:
    # followers_check()
    print(f"{users_score}")
else:
    print("Invalid input. Please try again!")

from replit import clear
clear()

from art import logo
print(logo)

print(retain_personality)
test_personality = []
test_personality.append(retain_personality)
retained_personality = test_personality[0]
name = retain_personality['name']
description = retained_personality['description']
country = retained_personality['country']

print(f"Compare A: {name}, {description}, {country}")

from art import vs
print(vs)

# Random person 2 picked
followers, personality, name, description, country = random_person() 
followers_b = followers
personality_b = personality
print(followers)
# print(personality)
print(f"Compare B: {name}, {description}, {country}")
