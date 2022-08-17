from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

play_game = True

while play_game:

    screen.update()
    time.sleep(0.001)
    ball.move_ball()



screen.exitonclick()