# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# if right_is_clear():
#     turn_right()
#     move()
# elif wall_in_front():
#     turn_right()


# Solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# When you get better, come back to this and debug th infinite loop problem in the problem_world (Reeborg World Tests). Come back after Day 15