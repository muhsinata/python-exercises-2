import turtle as t
import time


class Snake:

    def __init__(self):
        self.coordinate_x = 0
        self.coordinate_y = 0
        self.sqr_num = 3
        self.square_list = []
        self.keep_playing = True
        self.screen_tracer = t.Screen().tracer(0)
        self.screen_background = t.Screen().bgcolor("black")
        self.create_squares(3)

    def create_squares(self, sqr_num):
        for square_num in range(sqr_num):
            square = t.Turtle("square")
            square.color("white")
            square.penup()
            square.goto(x=self.coordinate_x, y=self.coordinate_y)
            self.coordinate_x -= 20
            self.square_list.append(square)

    def start_game(self):
        while self.keep_playing:
            t.Screen().update()
            time.sleep(0.1)
            for square_num in range(len(self.square_list) - 1, 0, -1):
                new_x = self.square_list[square_num - 1].xcor()
                new_y = self.square_list[square_num - 1].ycor()
                self.square_list[square_num].goto(x=new_x, y=new_y)
            self.square_list[0].forward(20)
