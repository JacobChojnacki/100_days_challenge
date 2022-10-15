from turtle import Turtle


class Scoreboad(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.shape('blank')
        self.goto(0, 250)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_score} : {self.r_score}",
                   move=False,
                   align='center',
                   font=('Calibre', 15, 'normal'))

    def left_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def right_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()