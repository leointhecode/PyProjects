from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 19, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.goto(0, 260)
        self.color("white")
        self.score = 0
        with open("data.txt") as data_0:
            self.high_score = int(data_0.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, 260)

    def count_score(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def new_high_score(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))
