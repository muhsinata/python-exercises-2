from turtle import Turtle

FONT = ("Courier", 8, "normal")


class WriteState(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")

    def find_state(self, x, y):
        self.goto(x, y)

    def write_state_name(self, state_name):
        self.write(state_name, align="center", font=FONT)

