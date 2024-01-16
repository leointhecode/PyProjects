from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 28, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.goto(0, 210)
        self.color("white")
        self.score = 0
        self.otherScore = 0
        self.count_score()

    def count_score(self):
        self.clear()
        self.goto(0, 210)
        self.write(f"  PONG\n {self.score}         {self.otherScore} ", move=False, align=ALIGNMENT, font=FONT)
        self.create_board()

    def create_board(self):
        self.pu()
        self.setheading(90)
        self.goto(0, 250)
        self.pensize(4)

        for n in range(27):
            self.pendown()
            self.back(10)
            self.penup()
            self.back(10)

    def user_point(self):
        self.score += 1

    def adv_point(self):
        self.otherScore += 1
