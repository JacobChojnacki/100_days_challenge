import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=500, height=500)
screen.tracer(0)

# Setup player
player = Player()

# Setup cars
car_manager = CarManager()

# Setup scoreboard
scoreboard = Scoreboard()

# Control
screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.car_list:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 240:
        scoreboard.add_point()
        player.reset()
        car_manager.next_level()


screen.exitonclick()

