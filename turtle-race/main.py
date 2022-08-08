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

while race_continues:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
    for turtle in turtles:
        if turtle.xcor() >= 215:
            winners.append(turtle)
    if len(winners) > 0:
        race_continues = False

for winner in range(len(winners)):
    print(f"Winner{winner + 1}: {list(winners[winner].color())[winner]} turtle.")
    if list(winners[winner].color())[winner] == user_bet:
        print("You win the bet!")
    else:
        print("You lost the bet.")


screen.exitonclick()