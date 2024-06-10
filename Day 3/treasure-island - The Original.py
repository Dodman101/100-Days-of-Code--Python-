# You can get ASCII art on the site below
#TODO: Get and ASCII art at - "ascii.co.uk/art/", and then formulate an interesting story.

#? Hints:
#? Use a flowchart diagram to aid in story formulation

#! Story:
''' 
    You are a soldier returning from a war that lasted 5 years.
    Two options are provided to you: "Go back home" or "Return to Military Camp" ,type left for camp and right for home

    Military Camp (left): 
    You are awarded the highest honor and rank. Accept a mission or choose a desk job ? Type mission or desk. 
    "mission" - You had a mole in your team, got ambushed and shot dead. Game over. 
    "desk" - You get wealthy. Continue with regular exercises ? Y or N . 
        "Y" - live to 90 and die of old age. Game over!. 
        "N" - Be obese and die before 50 because of lifestyle diseases. Game Over!.

    Home (right):
    You find new people, some of your friends have passed on and others have left the village in search of greener pasture in the City. Type Village or City.
    "village" - You start small scale farming, a drought strikes the land and you die of hunger. Game Over!
    "city" - You arrive to the city, you are rejoined with your friends and now you have to choose between spending time with your Friends or  Working ?
        "friends" - Your morals get corrupted, end up in jail. Game Over!
        "working" - Gain wealth and status in the society. Game Over!

'''

#* Algorithm
#* Introduce the player into the game (Welcome to "The Original")
#* Get input from the user "right" or "left"
#* Use an if / else, nested ifs and elif statements to check the input and proceed accordingly


# Start
print("Welcome to 'The Original' \n")
#Army
print(
'''        ,adPPYYba, 8b,dPPYba, 88,dPYba,,adPYba,  8b       d8  
        ""     `Y8 88P'   "Y8 88P'   "88"    "8a `8b     d8'  
        ,adPPPPP88 88         88      88      88  `8b   d8'   
        88,    ,88 88         88      88      88   `8b,d8'    
        `"8bbdP"Y8 88         88      88      88     Y88'     
                                                    d8'      
                                                    d8'  
\n''' 
)

print("You are a soldier returning from a war that lasted 5 years.\n")
choice1 = input("You have two options available for you. Type 'right' to Go Home, and 'left' to Return to Base Camp.: \n")
choice1_lower = choice1.lower()

#Home

if (choice1_lower == "right"):
    print("You find new people, some of your friends have passed on and others have left the village in search of greener pasture in the City.\n")

    choice2 = input("Type 'village' to stay in your village or 'city' to follow your frineds: \n")
    choice2_lower = choice2.lower()

    if (choice2_lower == 'village'):    
        print("You start small scale farming, a drought strikes the land and you die of hunger. Game Over! \n")
    elif (choice2_lower =="city"):
        print("You arrive to the city, you are rejoined with your friends \n")

        print('''                   _________
              |MMMMMMMMM|                _
  ________    |MMMMMMMMM|              _|l|_
 |!!!!!!!_|___|MMMMMMMMM|             |lllll|
 |!!!!!!|=========|MMMMM|             |lllll|_______
 |!!!!!!|=========|MMMMM|            _|lllll|HHHHHHH|
 |!!!!!!|=========|MMMMM|   ________|lllllllll|HHHHH|
 |!!!!!!|=========|MMMMM|  |unununun|lllllllll|HHHHH|______
 |!!!!!!|=========|MMMMM|  |nunununu|lllllllll|HH|:::::::::|
 |!!!!!!|=========|MMM__|..|un__unun|lllllllll|HH|:::::::::|
 |!!!!!!|=======_=|M_( ')' );' .)unu|lllllllll|HH|:::::::::|
 |!!!_!!|======( )|(. ` ,) (_ ', )un|lllllllll|HH|:::::::::| ~~~
 |!!(.)!|===__(`.')_(_ ')_,)(. _)unu|lllllllll|HH|:__::::::|~~  ~~
 |!(.`')|==( .)' .)MMM|M|| |un|nunun|lllllllll|``|( ,)_::::| ~~~~ ~
  -(: _)|=(`. ')_)|---|- '  ``|`````|lll____ll|  (_; `'):::|~~~  ~~~
     |  |==(_'_)|=|    ______        ''/\   \'   |(_'_)::::|\~~~~__|)__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\n ''')
        choice3 = input("Type 'friends' to spend time with your Friends or 'working' to get a job.\n")
        choice3_lower = choice3.lower()

        if (choice3_lower == 'friends'):
            print("Your morals get corrupted and you end up in jail. Game Over! \n")
        elif (choice3_lower == 'working'):
            print("Gain wealth and status in the society. You win! \n")

#Millitary
  
elif (choice1_lower == 'left'):
    print('''

                      \|/
                      -o-                              |
                      /|\                             ( )_
             |                                       /\ | |
            (_)             |      |   __         |  ||-| |-[]|  \|/  \|
 ___|___   _| |____   |    (_)_  _( )_|[]|     __(_)_|| |     |_~(|)~~(|
(_)__)__|_| []|[]  |_(_)_  |[]|_|_[]__|__|  __| |[]|__| | []|___|_|____|
| |__| [] |   |[]  |  | |  |    | []  |  | |  | |   |||_|    [][]      |

Frankfurt AirBase \n
''')
    print("You are awarded the highest honor and rank for being brave enough to go back to the army. \n")

    choice4 = input("Type 'mission' to accept a mission or 'desk' choose a desk job ? \n")
    choice4_lower = choice4.lower()

    if (choice4_lower == 'mission'):
        print("You had a mole in your team, got ambushed and shot dead. Game over!.\n")

    elif (choice4_lower == 'desk'):
        print("You get really wealthy. \n")

        choice5 = input("Type 'Yes' to continue with regular exercises or 'No' to stop: \n")
        choice5_lower = choice5.lower()
        if (choice5_lower == 'yes'):
            print("You live to 90 and die of old age. You win! \n")
        elif (choice5_lower == 'no'):
            print("You get obese and die before 50 because of lifestyle diseases. Game Over!.\n")



