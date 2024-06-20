MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

machine_on = True
while machine_on:
    # TODO - 1: Print report of coffee machine resources
    order = input("What would you like? (espresso/latte/cappuccino)")
    #  TODO - 2: Check if resources are sufficient

    def remaining_resources():
        """Returns remaining resources when an order is made"""
        resources["water"] = remaining_water
        resources["milk"] = remaining_milk
        resources["coffee"] = remaining_coffee
        return f"water: {resources["water"]}, milk: {resources["milk"]}, coffee: {resources["coffee"]}"

    def enough_resources(ingredients):
        """Check if remaining resources are enough for the order placed"""
        for item in ingredients:
            if ingredients[item] > resources[item] or resources[item] <= 0:
                print(f"Sorry there is not enough {item}.")
                return False
        return True


    def calculate():
        print("Please insert coins. ")
        coin_values = {
            "penny": 0.01,
            "dime": 0.10,
            "nickel": 0.05,
            "quarter": 0.25
        }
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickels = int(input("How many nickels?"))
        pennies = int(input("How many pennies?"))
        total_inputs = ((coin_values["penny"] * pennies) + (coin_values["dime"] * dimes) +
                        (coin_values["nickel"] * nickels) + (coin_values["quarter"] * quarters))
        # resources["money"] = 0
    

        if order == "espresso" and total_inputs > MENU["espresso"]["cost"]:
            resources["money"] += MENU["espresso"]["cost"]
            change = (total_inputs - MENU["espresso"]["cost"])
            rounded_change = round(change, 2)
            return f"An espresso costs ${MENU["espresso"]["cost"]}. Here is your change: ${rounded_change}"
        elif order == "espresso" and total_inputs < MENU["espresso"]["cost"]:
            return (f"Sorry, an espresso costs ${MENU["espresso"]["cost"]} and you have put ${total_inputs}."
                    f" Here is your refund.")
        elif order == "latte" and total_inputs > MENU["latte"]["cost"]:
            resources["money"] += MENU["latte"]["cost"]
            change = (total_inputs - MENU["latte"]["cost"])
            rounded_change = round(change, 2)
            return f"A latte costs ${MENU["latte"]["cost"]}. Here is your change: ${rounded_change}"
        elif order == "latte" and total_inputs < MENU["latte"]["cost"]:
            return (f"Sorry, a latte costs ${MENU["latte"]["cost"]} and you have put ${total_inputs}."
                    f" Here is your refund")
        elif order == "cappuccino" and total_inputs > MENU["cappuccino"]["cost"]:
            resources["money"] += MENU["cappuccino"]["cost"]
            change = (total_inputs - MENU["cappuccino"]["cost"])
            rounded_change = round(change, 2)
            return f"A capuccino costs ${MENU["cappuccino"]["cost"]}. Here is ${rounded_change} in change"
        elif order == "cappuccino" and total_inputs < MENU["cappuccino"]["cost"]:
            return (f"Sorry, a capuccino costs ${MENU["cappuccino"]["cost"]} and you have put ${total_inputs}."
                    f" Here is your refund ")
        else:
            return total_inputs


    if order == "report":
        for keys, values in resources.items():
            if keys == "money":
                print(f"{keys}: ${values:.2f}")
            elif keys == "coffee":
                print(f"{keys}: {values} g")
            else:
                print(f"{keys}: {values} ml")
        # break
    elif order == "off":
        machine_on = False
        break
    else:
        order_made = True
        while order_made:
            # Updates the amount of resources left
            menu_items = order
            if menu_items == "espresso":
                if enough_resources(ingredients=MENU["espresso"]["ingredients"]):
                    remaining_water = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                    print(remaining_water)
                    remaining_milk = resources["milk"]
                    remaining_coffee = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]

                    print(remaining_resources())
                    print(calculate())
                    break
                else:
                    print("Not enough resources. Please try again.")
                    break

            elif menu_items == "latte":
                if enough_resources(MENU["latte"]["ingredients"]):
                    remaining_water = resources["water"] - MENU["latte"]["ingredients"]["water"]
                    remaining_milk = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                    remaining_coffee = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                    print(remaining_resources())
                    print(calculate())
                    break
                else:
                    print("Not enough resources. Please try again.")
                    break
            elif menu_items == "cappuccino":
                if enough_resources(MENU["cappuccino"]["ingredients"]):
                    remaining_water = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                    remaining_milk = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                    remaining_coffee = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                    print(remaining_resources())
                    print(calculate())
                    break
                else:
                    print("Not enough resources. Please try again.")
                    break
            order_made = False

    #  TODO - 3: Process coins

    # Calculates the total cost of the coins placed in and outputs change if need be.
    # The condition that has to be met in-order for coins to be processed in that;
    # The resources have to enough and the input has to be a drink
    #  TODO - 3: Check if transaction was successful
    #  TODO - 5: Make coffee

