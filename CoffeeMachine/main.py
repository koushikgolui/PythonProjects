from menu import resources
from menu import MENU

# TODO 1. print report


def print_report(remaining_resources, final_money):
    water_remaining = remaining_resources["water"]
    milk_remaining = remaining_resources["milk"]
    coffee_remaining = remaining_resources["coffee"]
    print(f"Water: {water_remaining}ml\nMilk: {milk_remaining}ml\nCoffee: {coffee_remaining}g\nMoney: ${final_money}")


def check_resources(remaining_resources, required_resources):
    for item in required_resources:
        if remaining_resources[item] < required_resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def update_resources(remaining_resources, required_resources):
    for item in required_resources:
        remaining_resources[item] -= required_resources[item]


def calculate_input_amount():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_amount = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return round(total_amount, 2)


# Declare variables:
money = 0
turn_off = False
resources_available = resources

# TODO 2. Request input from user
while not turn_off:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "report":
        print_report(resources_available, money)
    elif order == "off":
        turn_off = True
    elif order in ["espresso", "latte", "cappuccino"]:
        required_ingredients = MENU[order]["ingredients"]
        list_price = MENU[order]["cost"]

        enough_resources = check_resources(resources_available, required_ingredients)
        if enough_resources:
            customer_amount = calculate_input_amount()
            if list_price > customer_amount:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Enjoy your hot cup of ☕ {order}")
                update_resources(resources_available, required_ingredients)
                money += list_price
                refund_amount = round(customer_amount - list_price, 2)
                print(f"Here is your ${refund_amount} in change.")


