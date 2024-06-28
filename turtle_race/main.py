from turtle import Turtle, Screen
import random

# Constants for the screen size
WIDTH = 500
HEIGHT = 400

# Set up the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)

# Ask the user for their bet on which turtle will win the race
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

# Define the colors for the turtles
colors = ["red", "orange", "violet", "green", "blue", "purple"]
all_turtles = []

# Variable to check if the race is on
is_race_on = False

def create_turtle():
    """Creates turtles and positions them at the starting line."""
    gap = HEIGHT / (len(colors) + 1)
    y_position = -200 + gap
    x_position = -WIDTH / 2 + 30
    for turtle_index in range(len(colors)):
        a_turtle = Turtle(shape="turtle")
        a_turtle.color(colors[turtle_index])
        a_turtle.penup()
        a_turtle.goto(x_position, y_position)
        y_position += gap
        all_turtles.append(a_turtle)

# Start the race if the user has placed a bet
if user_bet:
    is_race_on = True

# Create the turtles
create_turtle()

# Run the race
while is_race_on:
    screen.update()
    for turtle in all_turtles:
        if turtle.xcor() >= WIDTH/2 - 5:
            winner = colors[all_turtles.index(turtle)]
            is_race_on = False
            break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Create a turtle to display the result
result_turtle = Turtle()
result_turtle.hideturtle()
result_turtle.penup()
result_turtle.goto(0, 0)

# Announce the winner on the screen
if winner == user_bet:
    result_turtle.write(f"Congratulations! The {winner} turtle has won the race!", align="center", font=("Arial", 16, "normal"))
else:
    result_turtle.write(f"Sorry, you lose! The {winner} turtle has won the race!", align="center", font=("Arial", 16, "normal"))

# Exit the screen on click
screen.exitonclick()
