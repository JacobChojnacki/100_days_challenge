from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape('blank')
        self.goto(0, 250)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",
                   move=False,
                   align='center',
                   font=('Calibre', 15, 'normal'))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER",
                   move=False,
                   align='center',
                   font=('Calibre', 15, 'normal'))

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
