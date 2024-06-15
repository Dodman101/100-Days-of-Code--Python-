from data import MENU
from data import resources

#TODO-1: Prompt the user by asking "What would you like? (espresso/latte/cappuccino):"
user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
#Check the user input to decide what to do next.
if user_input == espresso:
    print("Espresso logic")
elif user_input == latte:
    print("Latte logic")
elif user_input == cappuccino:
    print("")
#!Note: This prompt should show every time the action has completed. e.g Once the drink has been dispensed in order to serve the next customer.

#TODO-2: Turn off the Coffee Machine by entering "off" to the prompt. 
#? Your code execution should end when this happens.


#TODO-3: Print a report
#? It should be generated as below:
#? Water: 100ml
#? Milk: 50ml
#? Coffee: 76g
#? Money: $2.5


#TODO-4: Check if the resources are sufficient ?
#When the user chooses a drink, the program should check if there are enough resorces to make that drink.
#? E.g If Latte requires 200ml water but there is only 100ml left in the machine, it should not continue to make the drink but print: "Sorry there is not enough water. " . The same should happen if another resource is depleted. e.g Milk or Coffee


#TODO-5: Process the coins
#If there are sufficient resources to make the drink selected, then the program should prompt the user to enter coins.
#! Remember that quaters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#Calculate the monetary value of the coins inserted. 
#? E.g 1 quater, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1*1 + 0.05 + 0.01*2 = $0.52


#TODO-6: Check if the transaction is successful ?
#Check that the user has inserted enough money to purchase the drink they selected.
#? E.g Latte costs $2.50, but the only inserted $0.52, then after counting the coins the program should say "Sorry that's not enough money. Money refunded."

#But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time "report" is triggered. 
#? E.g 
#? Water: 100ml
#? Milk: 50ml
#? Coffee: 76g
#? Money: $2.5

#If the user has inserted too much money, the machine should offer change.
#? E.g "Here is $2.45 dollars in change." 
#! The change should be rounded to 2 decimal places. 


#TODO-7: Make Coffee
#If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
#? E.g Report before purchasing latte:
#? Water: 300ml
#? Milk: 200ml
#? Coffee: 100g
#? Money: $0

#? Report after purchasing latte:
#? Water: 100ml
#? Milk: 50ml
#? Coffee: 76g
#? Money: $2.5

#Once all resources have been deducted, tell the user "Here is your latte☕. Enjoy!" .
#! If latte was their choice of drink.