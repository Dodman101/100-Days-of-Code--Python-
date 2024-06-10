from replit import clear
from art import logo

print(logo)

print("Welcome to the secret biding platform !")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    user_prompt = input("Are there any other bidders? Type 'yes' or 'no'.")
    if user_prompt == "no":
        find_highest_bidder(bids)
        bidding_finished = True
    elif user_prompt == "yes":
        clear()


#! Use pythontutor.com to also visualize code online if not using Thonny





        

