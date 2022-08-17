from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0

    def show_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, font=("Courier", 80, "normal"))

    def update_r_score(self):
        self.r_score += 1

    def update_l_score(self):
        self.l_score += 1


