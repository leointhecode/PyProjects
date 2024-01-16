import turtle as t
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.snake_len = 3
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for n in range(0, self.snake_len):
            self.add_segment()

    def add_segment(self):
        seg = t.Turtle(shape="square")
        self.segments.append(seg)
        seg.goto(self.segments[len(self.segments) - 2].position())
        print(self.segments[-1].position())
        seg.color("white")
        seg.pu()

    def move(self):
        for n in range((len(self.segments) - 1), 0, -1):
            new_x = self.segments[n - 1].xcor()
            new_y = self.segments[n - 1].ycor()
            self.segments[n].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]