from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

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
    time.sleep(ball.move_speed)
    ball.move_ball()
    scoreboard.show_scoreboard()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_l_score()
        ball.increase_ball_speed()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_r_score()
        ball.increase_ball_speed()

screen.exitonclick()

