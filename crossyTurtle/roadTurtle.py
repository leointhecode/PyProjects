from turtle import Turtle

STARTING_POS = (0, -270)
MOVING_STEPS = 10


class RoadTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.goto(STARTING_POS)

    def move(self):
        self.forward(MOVING_STEPS)
