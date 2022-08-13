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
        self.screen = t.Screen()
        self.head = self.square_list[0]

    def create_squares(self, sqr_num):
        for square_num in range(sqr_num):
            square = t.Turtle("square")
            square.color("white")
            square.penup()
            square.goto(x=self.coordinate_x, y=self.coordinate_y)
            self.coordinate_x -= 20
            self.square_list.append(square)

    def start_game(self, food_obj, scoreboard):

        while self.keep_playing:

            t.Screen().update()
            time.sleep(0.1)

            for square_num in range(len(self.square_list) - 1, 0, -1):
                new_x = self.square_list[square_num - 1].xcor()
                new_y = self.square_list[square_num - 1].ycor()
                self.square_list[square_num].goto(x=new_x, y=new_y)
            self.head.forward(20)

            self.screen.listen()
            self.screen.onkey(self.move_left, "Left")
            self.screen.onkey(self.move_right, "Right")
            self.screen.onkey(self.move_down, "Down")
            self.screen.onkey(self.move_up, "Up")

            if self.head.distance(food_obj) < 15:
                food_obj.refresh()
                scoreboard.clear()
                scoreboard.score += 1
                scoreboard.score_screen()

            if self.head.xcor() < -290 or self.head.xcor() > 290 or self.head.ycor() < -290 or self.head.ycor() > 290:
                self.keep_playing = False
                scoreboard.game_over()

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

