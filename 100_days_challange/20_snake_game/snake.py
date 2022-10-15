from turtle import Turtle

STARTING_POINTS = [(0, 0), (-20, 0), (-40, 0)]
SPEED_SNAKE = 20
DIRECTION = [0, 90, 180, 270]
parts_of_our_snake = []


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.speed_snake = 20
        self.create_snake()

    def reset(self):
        [part.reset() for part in self.snake_parts]
        self.snake_parts = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POINTS:
            self.new_part(position)

    def new_part(self, position):
        jacob_part = Turtle('square')
        jacob_part.color("white")
        jacob_part.penup()
        jacob_part.goto(position)
        self.snake_parts.append(jacob_part)

    def growing(self):
        self.new_part(self.snake_parts[-1].position())

    def move(self):
        for snake_part in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[snake_part - 1].xcor()
            new_y = self.snake_parts[snake_part - 1].ycor()
            self.snake_parts[snake_part].goto(new_x, new_y)
        self.snake_parts[0].forward(SPEED_SNAKE)

    def up(self):
        if self.snake_parts[0].heading() != DIRECTION[3]:
            self.snake_parts[0].setheading(DIRECTION[1])

    def down(self):
        if self.snake_parts[0].heading() != DIRECTION[1]:
            self.snake_parts[0].setheading(DIRECTION[3])

    def left(self):
        if self.snake_parts[0].heading() != DIRECTION[0]:
            self.snake_parts[0].setheading(DIRECTION[2])

    def right(self):
        if self.snake_parts[0].heading() != DIRECTION[2]:
            self.snake_parts[0].setheading(DIRECTION[0])
