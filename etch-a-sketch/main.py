import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
t.onkey(move_forward, "w")
t.onkey(move_backward, "s")
t.onkey(turn_right, "d")
t.onkey(turn_left, "a")
t.onkey(clear, "c")

screen.exitonclick()
