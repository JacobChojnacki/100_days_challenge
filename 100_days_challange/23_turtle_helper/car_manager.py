from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.starting_move_distance = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT

    def create_car(self):
        chance_to_generate_car = random.randint(0, 2)
        if chance_to_generate_car == 2:
            new_car = Turtle()
            new_car.shape('square')
            new_car.color(random.choice(COLORS))
            new_car.left(180)
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.goto(250, random.randint(-200, 250))
            self.car_list.append(new_car)

    def move(self):
        [car.forward(self.starting_move_distance) for car in self.car_list]

    def next_level(self):
        self.starting_move_distance += self.move_increment
        [car.reset() for car in self.car_list]
        self.car_list = []
