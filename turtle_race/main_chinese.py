from turtle import Turtle, Screen
import random

# Constants for the screen size
WIDTH = 1000
HEIGHT = 1000

# Set up the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)

# Define the colors for the turtles
colors = ["红", "橙", "粉", "绿", "蓝", "紫"]
all_turtles = []

# Variable to check if the race is on
is_race_on = False


def get_color(c_text):
    if c_text in colors:
        if c_text == "红":
            e_text = "red"
        if c_text == "橙":
            e_text = "orange"
        if c_text == "粉":
            e_text = "violet"
        if c_text == "绿":
            e_text = "green"
        if c_text == "蓝":
            e_text = "blue"
        if c_text == "紫":
            e_text = "purple"
    return e_text


def create_turtle():
    """Creates turtles and positions them at the starting line."""
    gap = HEIGHT / (len(colors) + 1)
    y_position = -HEIGHT / 2 + gap
    x_position = -WIDTH / 2 + 30
    for turtle_index in range(len(colors)):
        a_turtle = Turtle(shape="turtle")
        a_turtle.speed(8)
        a_turtle.color(get_color(colors[turtle_index]))
        a_turtle.penup()
        a_turtle.goto(x_position, y_position)
        y_position += gap
        all_turtles.append(a_turtle)


# Create the turtles
create_turtle()
# Ask the user for their bet on which turtle will win the race
user_bet = screen.textinput(title="Make your bet", prompt="哪一只龟会赢？（红，橙，粉，绿，蓝，紫）: ")

# Start the race if the user has placed a bet
if user_bet:
    is_race_on = True

# Run the race
while is_race_on:
    screen.update()
    for turtle in all_turtles:
        if turtle.xcor() >= WIDTH / 2 - 5:
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
    result_turtle.write(f"恭喜!猜对了！ {winner}小龟赢得了胜利!", align="center", font=("Arial", 32, "normal"))
else:
    result_turtle.write(f"您输了!  {winner}小龟赢得了胜利!", align="center", font=("Arial", 32, "normal"))

# Exit the screen on click
screen.exitonclick()
