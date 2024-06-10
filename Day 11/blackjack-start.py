############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from art import logo

def start_game():

    print(logo)

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        random_card = random.choice(cards)
        # print(random_card)
        return random_card

    deal_card()

    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    #user_cards = []
    #computer_cards = []
    # def start_cards():
    #     cards_dealt = []
    #     for card in range(2):
    #         deal_card()
    #         cards_dealt.append(deal_card())
    #     # print(cards_dealt)
    #     return cards_dealt

    user_cards = []
    for card in range(2):
            deal_card()
            user_cards.append(deal_card())
    print(f"Your cards: {user_cards}")

    computer_cards = []
    for card in range(2):
            deal_card()
            computer_cards.append(deal_card())
    print(f"Computer's first card: {computer_cards[0]}")

    #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
    #and returns the score. 
    #Look up the sum() function to help you do this.
    def calculate_score(cards_list):
        score = sum(cards_list)
        # print(score)
        #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
        if len(cards_list) == 2:
            if (11 in cards_list and 10 in cards_list):
                score = 0
                # return score     
            #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
            elif (11 in cards_list and score > 21):
                cards_list.remove(11)
                print(f"Cards after removing 11 {cards_list}")
                cards_list.append(1)
                print(f"Cards after adding 1 {cards_list}")
        return score      
    

    end_game = False

    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while not end_game:

    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        human_score = calculate_score(cards_list=user_cards)
        print(f"Your score is: {human_score}")
        computer_score = calculate_score(cards_list=computer_cards)
        # print(f"The computer's score is: {computer_score}")

        if (human_score == 0 or computer_score == 0 or human_score > 21):
            end_game = True
            # print("The game has ended!") 

        #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended. 
        else:
            decision = input('Do you want to draw another card. Type "yes" to draw or "no" to end the game? ' )
            if decision == "yes":
                user_cards.append(deal_card())
                print(f"Your cards after dealing another: {user_cards}")
                rechecked_cards = calculate_score(cards_list=user_cards)
                print(f"Human score after drawing a card is: {rechecked_cards}")

            elif decision == "no":
                end_game = True
                # print("The game has ended!")
            else:
                print("Invalid input! Please try again.")  


    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    computers_turn = False

    while not computers_turn:
        if computer_score < 17 and computer_score != 0:
            computer_cards.append(deal_card())
            print(computer_cards)
            computer_score = calculate_score(computer_cards)
            # print(computer_score)
        else:
            computers_turn = True

    #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
    def compare(human, computer):
        if human == computer:
            print("It's a draw!")
        elif computer == 0 or human > 21:
            print("The computer wins!")
        elif human == 0 or computer > 21:
            print("You win!")
        else:
            if human > computer:
                print("You win!")
            elif computer > human:
                print("The computer wins!") 

    compare(human_score, computer_score)

start_game()

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
restart_game = False

while not restart_game:
    restart = input("Do you want to restart the game? Type 'yes' to restart or 'no' to exit the game. ")

    if restart == "yes":
        from replit import clear
        clear()
        
        start_game()

    else:
        restart_game = True

