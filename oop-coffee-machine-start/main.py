from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create required objects

# menu_item = MenuItem()
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# declare variables

turn_off = False

while not turn_off:
    # take user input
    choice = input(f"What would you like? ({menu.get_items()}):").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        turn_off = True
    else:
        drink = menu.find_drink(choice)
        if drink:
            can_make = coffee_maker.is_resource_sufficient(drink)
            if can_make:
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)



