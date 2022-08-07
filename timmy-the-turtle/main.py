import random
import colorgram as cg
import turtle as t

tim = t.Turtle()
screen = t.Screen()
tim.speed("fastest")

colors = cg.extract("hirst.jpg", 30)
color_list = [(224, 150, 101), (176, 156, 101), (71, 92, 108), (138, 133, 131), (238, 215, 161),
              (247, 239, 210), (205, 139, 98),  (239, 134, 119), (160, 231, 125), (130, 182, 217),
              (240, 130, 172), (188, 171, 252), (85, 123, 63), (255, 217, 100), (247, 231, 195)]

screen.colormode(255)

# def extract_colors():
#
#     for _ in range(6):
#         color_list.append(tuple(colors[_].rgb))
#
#
# extract_colors()

tim.hideturtle()
tim.penup()
tim.right(180)
tim.forward(250)
tim.left(90)
tim.forward(250)
tim.left(90)

for _ in range(10):
    for line in range(10):
        dot_color = random.choice(color_list)
        tim.dot(20, dot_color)
        tim.color(dot_color)
        tim.penup()
        tim.forward(50)
    tim.right(180)
    tim.forward(500)
    tim.right(90)
    tim.forward(50)
    tim.right(90)

screen.exitonclick()