from turtle import Turtle

WIDTH = 20
HEIGHT = 100


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        move = self.ycor() + 20
        self.goto(self.xcor(), move)

    def down(self):
        move = self.ycor() - 20
        self.goto(self.xcor(), move)
