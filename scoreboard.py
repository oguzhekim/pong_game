from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 34, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.goto(0, 240)
        self.color("white")
        self.write(arg=f"{self.score1}     {self.score2}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
