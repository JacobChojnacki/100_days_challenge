from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.shape('blank')
        self.goto(0, 275)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score {self.high_score}",
                   move=False,
                   align='center',
                   font=('Calibre', 15, 'normal'))

    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER",
    #                move=False,
    #                align='center',
    #                font=('Calibre', 15, 'normal'))

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def highest_score(self):
        self.high_score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.clear()
        self.update_scoreboard()