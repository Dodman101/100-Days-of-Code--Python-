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
        if water < espresso_required_water:
            print("Sorry there is not enough water.")
        elif coffee < espresso_required_coffee:
            print("Sorry there is not enough coffee.")
    elif drink == "latte":
        if water < latte_required_water:
            print("Sorry there is not enough water.")
        elif milk < latte_required_milk:
            print("Sorry there is not enough milk.")
        elif coffee < latte_required_coffee:
            print("Sorry there is not enough coffee.")
    elif drink == "cappuccino":
        if water < cappuccino_required_water:
            print("Sorry there is not enough water.")
        elif milk < cappuccino_required_milk:
            print("Sorry there is not enough milk.")
        elif coffee < cappuccino_required_coffee:
            print("Sorry there is not enough coffee.")
    else:
        print("No drink specified")


def process_coins():
    """Returns the total value of the coins inserted"""
    print("Please insert coins: ")
    quaters = float(input("Quaters: "))
    dimes = float(input("Dimes: "))
    nickels = float(input("Nickels: "))
    pennies = float(input("Pennies: "))
    coin_value = ((quaters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01))
    return coin_value


def make_coffee():
    global water
    global coffee
    global milk
    global money

    make_coffee == True
    while make_coffee:
        if user_input == "espresso" and monetary_value >= espresso_cost:
            water -= espresso_required_water
            coffee -= espresso_required_coffee
            milk_left = milk
            money += espresso_cost
            #Once all resources have been deducted, tell the user "Here is your espresso☕. Enjoy!" .
                #! If espresso was their choice of drink.
            print(f"Here is your espresso☕. Enjoy!")
        elif user_input == "latte" and monetary_value >= latte_cost:
            water -= latte_required_water
            coffee -= latte_required_coffee
            milk -= latte_required_milk
            money += latte_cost
            #Once all resources have been deducted, tell the user "Here is your latte☕. Enjoy!" .
                #! If latte was their choice of drink.
            print(f"Here is your latte☕. Enjoy!")
        elif user_input == "cappuccino" and monetary_value >= cappuccino_cost:
            water -= cappuccino_required_water
            coffee -= cappuccino_required_coffee
            milk -= cappuccino_required_milk
            money += cappuccino_cost
            #Once all resources have been deducted, tell the user "Here is your cappuccino☕. Enjoy!" .
                #! If cappuccino was their choice of drink.
            print(f"Here is your cappuccino☕. Enjoy!")
        
        return water, milk, coffee, money

money = 0
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']

machine_off = False

while not machine_off:    
    espresso_cost = MENU["espresso"]["cost"]
    latte_cost = MENU["latte"]["cost"]
    cappuccino_cost = MENU["cappuccino"]["cost"]
    espresso_required_water = MENU["espresso"]["ingredients"]["water"]
    espresso_required_coffee = MENU["espresso"]["ingredients"]["coffee"]
    latte_required_water = MENU["latte"]["ingredients"]["water"]
    latte_required_coffee = MENU["latte"]["ingredients"]["coffee"]
    latte_required_milk = MENU["latte"]["ingredients"]["milk"]
    cappuccino_required_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_required_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    cappuccino_required_milk = MENU["cappuccino"]["ingredients"]["milk"]

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
        # machine_off = True 
    
    
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
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

        coin_value = process_coins()

        monetary_value = round(coin_value, 2)

        # print(f"${monetary_value}")

        #TODO-6: Check if the transaction is successful ?
        #Check that the user has inserted enough money to purchase the drink they selected.
        #? E.g Latte costs $2.50, but the only inserted $0.52, then after counting the coins the program should say "Sorry that's not enough money. Money refunded."
        if user_input == "espresso" and monetary_value < espresso_cost:
            print(f"Sorry, an espresso costs ${espresso_cost} and you have put ${monetary_value}. Here is your refund.")
            # machine_off = True
        elif user_input == "latte" and monetary_value < latte_cost:
            print(f"Sorry, a latte costs ${latte_cost} and you have put ${monetary_value}. Here is your refund.")
            # machine_off = True
        elif user_input == "cappuccino" and monetary_value < cappuccino_cost:
            print(f"Sorry, a cappuccino costs ${cappuccino_cost} and you have put ${monetary_value}. Here is your refund.")
            # machine_off = True
        else:
            #But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time "report" is triggered. 
            #? E.g 
            #? Water: 100ml
            #? Milk: 50ml
            #? Coffee: 76g
            #? Money: $2.5

            #If the user has inserted too much money, the machine should offer change.
            #? E.g "Here is $2.45 dollars in change." 
            #! The change should be rounded to 2 decimal places. 
            if user_input == "espresso" and monetary_value >= espresso_cost:
                change = round((monetary_value - espresso_cost), 2)
                print(f"An espresso costs ${espresso_cost}. Here is your change: ${change}")
            elif user_input == "latte" and monetary_value >= latte_cost:
                change = round((monetary_value - latte_cost), 2)
                print(f"An latte costs ${latte_cost}. Here is your change: ${change}")
            elif user_input == "cappuccino" and monetary_value >= cappuccino_cost:
                change = round((monetary_value - cappuccino_cost), 2)
                print(f"An cappuccino costs ${cappuccino_cost}. Here is your change: ${change}")
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
            water, milk, coffee, money = make_coffee()

            # report(water, milk, coffee, money)
    
    else:
        print("Invalid input!")
        machine_off = True

    