from turtle import Turtle, Screen
import random

WIDTH = 500
HEIGHT = 400

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "violet", "green", "blue", "purple"]
all_turtles = []

is_race_on = False


def create_turtle():
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


if user_bet:
    is_race_on = True

create_turtle()
while is_race_on:
    screen.update()
    for turtle in all_turtles:
        if turtle.xcor() >= WIDTH/2:
            winner = colors[all_turtles.index(turtle)]
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
if winner == user_bet:
    print(f"Congratulations! {winner} turtle have won the race!")
else:
    print(f"Sorry, you lose! {winner} turtle have won the race!")

screen.exitonclick()
