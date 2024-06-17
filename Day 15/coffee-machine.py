from data import MENU
from data import resources


def report(water, milk, coffee, money):
    """This function takes 4 inputs(water, milk, coffee, money) and then prints a report"""
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}")


def check_resources(drink):
    """This function takes an input drink and then checks to see whether there are resources available to make the specified drink"""
    if drink == "espresso":
        if water < 50:
            print("Sorry there is not enough water.")
        elif coffee < 18:
            print("Sorry there is not enough coffee.")
    elif drink == "latte":
        if water < 200:
            print("Sorry there is not enough water.")
        elif milk < 150:
            print("Sorry there is not enough milk.")
        elif coffee < 24:
            print("Sorry there is not enough coffee.")
    elif drink == "cappuccino":
        if water < 250:
            print("Sorry there is not enough water.")
        elif milk < 100:
            print("Sorry there is not enough milk.")
        elif coffee < 24:
            print("Sorry there is not enough coffee.")
    else:
        print("No drink specified")


def process_coins(quater, dime, nickel, penny):
    coin_value = ((quater * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01))
    return coin_value


def make_coffee():
    global water
    global coffee
    global milk

    if user_input == "espresso" and monetary_value >= 1.50:
        water -= 50
        coffee -= 18
        print(f"Here is your espresso☕. Enjoy!")
    elif user_input == "latte" and monetary_value >= 2.50:
        water -= 200
        coffee -= 24
        milk -= 150
        print(f"Here is your latte☕. Enjoy!")
    elif user_input == "cappuccino" and monetary_value >= 3.00:
        water -= 250
        coffee -= 24
        milk -= 100
        print(f"Here is your cappuccino☕. Enjoy!")
    
    return water, coffee, milk

machine_off = False

while not machine_off:

    money = 0
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']

    #TODO-1: Prompt the user by asking "What would you like? (espresso/latte/cappuccino):"
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    #Check the user input to decide what to do next.
    #TODO-2: Turn off the Coffee Machine by entering "off" to the prompt. 
    #? Your code execution should end when this happens.
    if user_input == "off":
        print("Machine switched off successfully")
        machine_off = True

    #TODO-3: Print a report
    #? It should be generated as below:
    #? Water: 100ml
    #? Milk: 50ml
    #? Coffee: 76g
    #? Money: $2.5
    elif user_input == "report":
        report(water, milk, coffee, money)
        machine_off = True
    
    elif user_input != "":
    #!Note: This prompt should show every time the action has completed. e.g Once the drink has been dispensed in order to serve the next customer.


        #TODO-4: Check if the resources are sufficient ?
        #When the user chooses a drink, the program should check if there are enough resorces to make that drink.
        #? E.g If Latte requires 200ml water but there is only 100ml left in the machine, it should not continue to make the drink but print: "Sorry there is not enough water. " . The same should happen if another resource is depleted. e.g Milk or Coffee
        check_resources(user_input)


        #TODO-5: Process the coins
        #If there are sufficient resources to make the drink selected, then the program should prompt the user to enter coins.
        #! Remember that quaters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        #Calculate the monetary value of the coins inserted. 
        #? E.g 1 quater, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1*1 + 0.05 + 0.01*2 = $0.52
        print("Please insert coins: ")
        quaters = float(input("Quaters: "))
        dimes = float(input("Dimes: "))
        nickels = float(input("Nickels: "))
        pennies = float(input("Pennies: "))

        coin_value = process_coins(quaters, dimes, nickels, pennies)

        monetary_value = round(coin_value, 2)

        print(f"${monetary_value}")

        #TODO-6: Check if the transaction is successful ?
        #Check that the user has inserted enough money to purchase the drink they selected.
        #? E.g Latte costs $2.50, but the only inserted $0.52, then after counting the coins the program should say "Sorry that's not enough money. Money refunded."
        if user_input == "espresso" and monetary_value < 1.50:
            print("Sorry that's not enough money. Money refunded.")
            machine_off = True
        elif user_input == "latte" and monetary_value < 2.50:
            print("Sorry that's not enough money. Money refunded.")
            machine_off = True
        elif user_input == "cappuccino" and monetary_value < 3.00:
            print("Sorry that's not enough money. Money refunded.")
            machine_off = True
        else:
            #But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time "report" is triggered. 
            #? E.g 
            #? Water: 100ml
            #? Milk: 50ml
            #? Coffee: 76g
            #? Money: $2.5
            money += monetary_value

            #If the user has inserted too much money, the machine should offer change.
            #? E.g "Here is $2.45 dollars in change." 
            #! The change should be rounded to 2 decimal places. 
            if user_input == "espresso" and monetary_value > 1.50:
                change = round((monetary_value - 1.50), 2)
                print(f"Here is ${change} dollars in change.")
            elif user_input == "latte" and monetary_value > 2.50:
                change = round((monetary_value - 2.50), 2)
                print(f"Here is ${change} dollars in change.")
            elif user_input == "cappuccino" and monetary_value > 3.00:
                change = round((monetary_value - 3.00), 2)
                print(f"Here is ${change} dollars in change.")

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
            make_coffee()

            #Once all resources have been deducted, tell the user "Here is your latte☕. Enjoy!" .
            #! If latte was their choice of drink.
            report(water, milk, coffee, money)
   
    else:
        print("Invalid input!")
        machine_off = True