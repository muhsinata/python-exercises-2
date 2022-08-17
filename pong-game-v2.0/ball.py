from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")

    def move_ball(self):
        self.setheading(45)
        self.forward(3)
