from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0, -220)
        self.left(90)
        self.y_move = 10

    def up(self):
        self.y_move += 1
        self.goto(self.xcor(), self.ycor() + self.y_move)

    def reset(self):
        self.goto(0, -220)
