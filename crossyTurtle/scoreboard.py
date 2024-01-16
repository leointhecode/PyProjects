from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240, 260)
        self.level = 0
        self.new_level()

    def new_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.home()
        self.write(f"    GAME OVER\nmaximum level: {self.level}", align=ALIGNMENT, font=FONT)

