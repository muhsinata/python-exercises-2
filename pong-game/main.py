import scoreboard
import turtle
import split_screen as ss

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SCREEN_COLOR = "black"

scoreboard = scoreboard.Scoreboard()
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)

ss.divide_screen()

screen.exitonclick()
