# Hurdles loop challenge
#Reeborgs world

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# def jump_hurdle():
#     #move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     turn_left()

#My idea
# def jump_hurdle():
#     while wall_in_front():
#         turn_left()
#         while wall_on_right():
#             move()
#             while right_is_clear():
#                 turn_right()
#                 move()
#                 turn_right()
#                 move()
# ----------------------------------

#? The solution
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    

# for step in range(6):
#     jump_hurdle()

# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump_hurdle()
#     number_of_hurdles -= 1

#Hurdle 2

# while not at_goal():
#     jump_hurdle()

#Hurdle 3

# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         jump_hurdle()
    
#Hurdle 4

# My Idea
# while not at_goal():
#     if front_is_clear:
#         move()
#         jump_hurdle()
#         turn_left()
# ----------------------

#? The solution
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
