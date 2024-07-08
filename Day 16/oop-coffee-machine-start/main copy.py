from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    coffee_names = menu.get_items()
    choice = input(f"What would you like. ({coffee_names}) ?").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        resources = coffee_maker.is_resource_sufficient(drink)
        cost = drink.cost
        if resources and money_machine.make_payment(cost):
            coffee_maker.make_coffee(drink)
