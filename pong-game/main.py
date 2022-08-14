import scoreboard
import turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SCREEN_COLOR = "black"

scoreboard = scoreboard.Scoreboard()
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)

screen_divider = turtle.Turtle()
screen_divider.hideturtle()
screen_divider.speed("fastest")
screen_divider.pencolor("white")
screen_divider.penup()
screen_divider.goto(0, SCREEN_HEIGHT/2)
screen_divider.pensize(5)
screen_divider.setheading(270)

keep_going = True

while keep_going:

    if screen_divider.distance(0, -SCREEN_HEIGHT/2) > 0:
        screen_divider.pendown()
        screen_divider.forward(10)
        screen_divider.penup()
        screen_divider.forward(10)
    else:
        keep_going = False

screen.exitonclick()
