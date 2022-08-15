import scoreboard
import turtle
import split_screen as ss
import paddles

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SCREEN_COLOR = "black"

scoreboard = scoreboard.Scoreboard()
paddle = paddles.Paddle()
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
paddle.move_pc_paddle()
ss.divide_screen()
screen.listen()


screen.exitonclick()
