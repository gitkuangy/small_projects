# Importing a module for displaying an ASCII art logo
from art import logo

# Defining basic arithmetic operation functions
def add(n1, n2):
    """Returns the sum of n1 and n2."""
    return n1 + n2

def subtract(n1, n2):
    """Returns the difference of n1 and n2."""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of n1 and n2."""
    return n1 * n2

def divide(n1, n2):
    """Returns the quotient of n1 divided by n2."""
    return n1 / n2

# Dictionary to map operators to their corresponding functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Display the logo
print(logo)

# Get the first two numbers from the user
num1 = float(input("What is your first number? "))
num2 = float(input("What is your second number? "))

# Display available operations
for operator in operations:
    print(operator)

# Get the operation from the user
operation = input("Pick an operation: ")

# Get the corresponding function from the dictionary
cal_func = operations[operation]

# Perform the first calculation
first_ans = cal_func(num1, num2)
print(f"{num1} {operation} {num2} = {first_ans}")

# Variable to control the continuation of the calculator
end_game = False

# Loop to continue calculations with the previous result
while not end_game:
    choose = input("Do you want to continue? (yes/no)\n")
    if choose == "no":
        end_game = True
    elif choose == "yes":
        num3 = float(input("What is your next number? "))
        operation = input("Pick an operation: ")
        cal_func = operations[operation]
        ans = cal_func(first_ans, num3)
        print(f"{first_ans} {operation} {num3} = {ans}")
        first_ans = ans
    else:
        print("Invalid input, please try again.")
