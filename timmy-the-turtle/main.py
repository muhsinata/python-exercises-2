import random
import colorgram as cg
import turtle as t

tim = t.Turtle()
screen = t.Screen()
tim.speed("fastest")

colors = cg.extract("hirst.jpg", 2**32)
color_list = []
screen.colormode(255)


def extract_colors():

    for _ in range(6):
        color_list.append(tuple(colors[_].rgb))


extract_colors()

tim.penup()
tim.right(180)
tim.forward(200)
tim.left(90)
tim.forward(200)
tim.left(90)

for _ in range(10):
    for line in range(10):
        tim.fillcolor(random.choice(color_list))
        tim.begin_fill()
        tim.color(random.choice(color_list))
        tim.circle(10)
        tim.end_fill()
        tim.penup()
        tim.forward(50)
    tim.right(180)
    tim.forward(500)
    tim.right(90)
    tim.forward(50)
    tim.right(90)

screen.exitonclick()

