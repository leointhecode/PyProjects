from turtle import Turtle
import random as r

CAR_VARIATION = [1.3, 1.8, 2.5, 2.9]
COLORS = ["blue", "red", "aqua", "orange", "pink", "purple"]
DISTANCE = [1, 5, 10, 15]
CARS = []
CAR_POS = 280


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = [self]
        self.shapesize(stretch_wid=1, stretch_len=r.choice(CAR_VARIATION))
        self.color(r.choice(COLORS))
        self.shape("square")
        self.resizemode("user")
        self.speed("fast")
        self.penup()
        self.setheading(180)
        self.goto(270, r.randint(-230, 250))

    def move(self):
        self.forward(r.choice(DISTANCE))

    def more_cars(self, num, chance):
        random_chance = r.randint(1, chance)
        if random_chance == 1:
            for n in range(num + 1):
                new_car = Cars()
                self.cars.append(new_car)
