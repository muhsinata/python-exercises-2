from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.coordinate_x = 0
        self.coordinate_y = 270
        self.score = 0
        self.goto(self.coordinate_x, self.coordinate_y)
        self.score_screen()

    def score_screen(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)