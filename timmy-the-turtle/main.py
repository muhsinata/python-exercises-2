import turtle as t

tim = t.Turtle()
tim.shape("turtle")

for sides in range(3, 10):
    for times in range(sides):
        tim.forward(100)
        tim.right(360/sides)







screen = t.Screen()
screen.exitonclick()
