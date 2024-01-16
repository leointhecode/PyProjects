from turtle import Turtle
import random as r
VARIATION = r.randint(45, 145)


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slow")
        self.setheading(50)

    def move(self):
        self.forward(5)

    def wall_bounce(self):
        difference = (360 - self.heading())
        self.setheading(difference)

    def pad_bounce(self):
        self.setheading(self.heading() + 270)
        self.setheading(self.heading() + 10)

    def refresh(self):
        self.home()
        self.setheading(VARIATION)
