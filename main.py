from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)


turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_coordinate = -80

turtles = []

index = 0
for color in turtle_colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinate)
    y_coordinate += 40
    turtles.append(new_turtle)
    index += 1

bet = screen.textinput("Make your bet", "Who will win the race? Enter a color: ")

play_game = True

while play_game:
    for y in range(len(turtles)):
        random_turtle = random.choice(turtles)
        random_turtle.forward(random.randint(0, 4))
        for turtle in turtles:
            if turtle.xcor() >= 250.0:
                play_game = False
                winner = turtle
                winning_color = turtle_colors[turtles.index(winner)]

if bet == winning_color:
    print(f"You guessed correctly! The winning color was {winning_color}!")
else:
    print(f"You guessed incorrectly. The winning color was {winning_color}.")

screen.exitonclick()
