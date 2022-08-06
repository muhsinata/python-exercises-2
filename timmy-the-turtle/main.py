import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

screen.colormode(255)
tim.shape("turtle")
tim.pensize(10)
tim.speed(10)

colors = [1, 2, 3]
turn = [90, -90, 180, 0]

for _ in range(150):

    for color in range(3):
        random_rgb_value = random.randint(1, 255)
        colors[color] = random_rgb_value

    tim.pencolor(colors[0], colors[1], colors[2])
    tim.right(random.choice(turn))
    tim.forward(22)

screen.exitonclick()









