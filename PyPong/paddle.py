from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.resizemode("user")
        self.pu()
        self.speed("fastest")
        self.setheading(90)
        self.goto(position)

    def up(self):
        if self.ycor() < 260:
            self.forward(20)

    def down(self):
        if self.ycor() > -260:
            self.back(20)
