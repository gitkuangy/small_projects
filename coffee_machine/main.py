from game_data import resources, MENU

# Initialize total money collected
money = 0


def coffee_machine_report():
    """Prints a report of the coffee machine's resources and money."""
    for item in resources:
        if item == "money":
            continue
        print(item.title() + ': ' + str(resources[item]), end="")
        if item == "water" or item == "milk":
            print("ml")
        elif item == "coffee":
            print("g")
    print(f"Money: ${money}")


def name_converter(name):
    """Converts user input to corresponding menu item name or reports."""
    if name == "r":
        coffee_machine_report()
    elif name == 'e':
        return 'espresso'
    elif name == 'l':
        return 'latte'
    elif name == 'c':
        return 'cappuccino'


coffee_enough = False
service_end = False


def check_quantity(coffee_name):
    """Checks if there are enough resources to make the selected coffee."""
    global coffee_enough

    if coffee_name in MENU:
        coffee_water = MENU[coffee_name]["ingredients"]["water"]
        coffee_milk = MENU[coffee_name]["ingredients"]["milk"]
        coffee_coffee = MENU[coffee_name]["ingredients"]["coffee"]
        machine_water = resources["water"]
        machine_milk = resources["milk"]
        machine_coffee = resources["coffee"]

        if coffee_water > machine_water:
            print("Sorry there is not enough water.")
        elif coffee_milk > machine_milk:
            print("Sorry there is not enough milk.")
        elif coffee_coffee > machine_coffee:
            print("Sorry there is not enough coffee.")
        else:
            coffee_enough = True


def coin_insert():
    """Calculates the total amount of money inserted by the user."""
    total_coin = 0
    cash = {"quarters": 0.25, "dimes": 0.1, "nickels": 0.05, "loonies": 1, "toonies": 2}
    print("Please insert coins.")
    for key in cash:
        money_quantity = int(input(f"How many {key}? "))
        coin_inserted = money_quantity * cash[key]
        total_coin += coin_inserted
    return total_coin


def service(coffee_name):
    """Handles the coffee making process including payment and serving."""
    global money
    coin_inserted = coin_insert()
    cost = MENU[coffee_name]["cost"]

    if coin_inserted < cost:
        print("Sorry that is not enough money. Money refunded")
    else:
        change = coin_inserted - cost
        print(f"Here is your change: ${change:.2f}.")
        print(f"Here is your {coffee_name}. Enjoy!")

        # Deduct resources used to make the coffee
        resources["water"] -= MENU[coffee_name]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee_name]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee_name]["ingredients"]["coffee"]
        money += cost


while not service_end:
    user_choice = input("What would you like to drink? (E-espresso, L-latte, C-cappuccino, R-report, X-exit): ").lower()
    coffee_choice = name_converter(user_choice)
    if user_choice == "r":
        continue
    if user_choice == "x":
        service_end = True
        print("Thanks for using this coffee service!")
        continue
    check_quantity(coffee_choice)
    if coffee_enough:
        service(coffee_choice)
        coffee_enough = False
