import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

screen.colormode(200)
tim.shape("turtle")
tim.pensize(10)
tim.speed(20)
screen.colormode(255)
turn = [90, -90, 180, 0]


def choose_color():

    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return (r, g, b)


for _ in range(150):

    tim.pencolor(choose_color())
    tim.right(random.choice(turn))
    tim.forward(22)

screen.exitonclick()