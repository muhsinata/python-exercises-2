import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make Your Bet", prompt="Which turtle will win the race? Enter its color: ")
colors = ["red", "blue", "purple", "green", "black", "brown"]
turtles = []

coordinate_x = -220
coordinate_y = -100

for turtle_num in range(6):
    turtle = t.Turtle(shape="turtle")
    turtle.color(colors[turtle_num])
    turtle.penup()
    turtle.goto(x=coordinate_x, y=coordinate_y)
    coordinate_y += 40
    turtle.speed("fastest")
    turtles.append(turtle)

race_continues = True

winners = []
winner_colors = []


def bet_result():
    if user_bet in winner_colors:
        print("You win the bet!")
    else:
        print("You lost the bet.")


while race_continues:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
    for turtle in turtles:
        if turtle.xcor() >= 220:
            winners.append(turtle)
    if len(winners) > 0:
        race_continues = False
        for winner in winners:
            turtle_color = winner.pencolor()
            winner_colors.append(turtle_color)
            print(f"Winner{winners.index(winner) + 1}: {turtle_color} turtle.")
            bet_result()

screen.exitonclick()

