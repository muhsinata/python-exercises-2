import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car

    for car in car_manager.car_list:
        if player.distance(car) < 20:
            print("Game Over")



