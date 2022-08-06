import random
import turtle as t

tim = t.Turtle()
screen = t.Screen()
tim.speed("fastest")
screen.colormode(255)


def choose_color():

    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return (r, g, b)


for _ in range(72):
    tim.color(choose_color())
    tim.circle(100)
    tim.left(5)

screen.exitonclick()