import turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_STRETCH_W = 5
PADDLE_STRETCH_H = 1
PADDLE_X_COR = 350
PADDLE_Y_COR = 0


screen = turtle.Screen()
paddle = turtle.Turtle()

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

paddle.shape("square")
paddle.shapesize(stretch_wid=PADDLE_STRETCH_W, stretch_len=PADDLE_STRETCH_H)
paddle.penup()
paddle.color("white")
paddle.goto(x=PADDLE_X_COR, y=PADDLE_Y_COR)


def move_up():
    new_y_cor = paddle.ycor() + 20
    paddle.goto(PADDLE_X_COR, new_y_cor)


def move_down():
    new_y_cor = paddle.ycor() - 20
    paddle.goto(PADDLE_X_COR, new_y_cor)


screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

play_game = True

while play_game:

    screen.update()
    




screen.exitonclick()