from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape('blank')
        self.color('black')
        self.penup()
        self.goto(-220, 210)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}",
                   move=False,
                   align='left',
                   font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER",
                   move=False,
                   align='center',
                   font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
