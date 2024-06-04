# Coffee Machine

This is a simple coffee machine simulator written in Python. The program allows users to choose from three types of coffee: espresso, latte, and cappuccino. Users can also check the machine's resource report and exit the program.

## Features

- Choose between espresso, latte, and cappuccino.
- Check the coffee machine's resources report.
- Insert coins to pay for the coffee.
- Receive change if overpaid.
- Resources are deducted when a coffee is made.
- Option to exit the program.

## Project Structure

- `main.py`: The main script to run the coffee machine program.
- `menu.py`: Contains the `Menu` and `MenuItem` classes to manage the menu items.
- `coffee_maker.py`: Contains the `CoffeeMaker` class to manage coffee making and resources.
- `money_machine.py`: Contains the `MoneyMachine` class to handle coin processing and payments.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/gitkuangy/small_projects.git
    cd coffee-machine
    ```

2. Create a `game_data.py` file in the same directory with the following content:
    ```python
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }

    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "milk": 0,
                "coffee": 18
            },
            "cost": 1.5
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24
            },
            "cost": 2.5
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 50,
                "coffee": 24
            },
            "cost": 3.0
        }
    }
    ```

3. Run the program:
    ```sh
    python main.py
    ```

4. Follow the prompts to interact with the coffee machine.

## Example

```plaintext
What would you like? (espresso/latte/cappuccino/)
Please insert coins.
How many quarters? 6
How many dimes? 0
How many nickels? 0
How many pennies? 0
Here is $0.50 in change.
Here is your latte ☕️. Enjoy!
What would you like? (espresso/latte/cappuccino/report/)
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
What would you like? (espresso/latte/cappuccino/report/)
Thanks for using this coffee service!
