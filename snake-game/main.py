import turtle as t
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

coordinate_x = 0
coordinate_y = 0

squares = []

for _ in range(3):
    square_num = t.Turtle("square")
    square_num.color("white")
    square_num.penup()
    square_num.goto(x=coordinate_x, y=coordinate_y)
    coordinate_x -= 20
    squares.append(square_num)

keep_playing = True

while keep_playing:

    screen.update()
    time.sleep(0.1)

    for square_num in range(len(squares) - 1, 0, -1):

        new_x = squares[square_num - 1].xcor()
        new_y = squares[square_num - 1].ycor()
        squares[square_num].goto(x=new_x, y=new_y)

    squares[0].forward(20)
    squares[0].left(90)









screen.exitonclick()