import turtle as t
import random as r


def create_turtle():
    name = t.Turtle(shape="turtle")
    name.speed("normal")
    name.shapesize(2, 2, 2)
    return name


def start_line(turtle_line, position):
    turtle_line.penup()
    turtle_line.setheading(210)
    turtle_line.forward(370)
    turtle_line.setheading(90)
    turtle_line.forward(position)
    turtle_line.right(90)


names = ["guy", "mirtle", "luffy", "loki", "tanaka", "klein", "ao_chan"]
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtles = [create_turtle() for n in names]
race = False

i = 0
for n in turtles:
    n.color(colors[i - 1])
    i += 1

screen = t.Screen()
screen.setup(width=680, height=370)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

count = 0
for n in turtles:
    count += 50
    start_line(n, count)

if user_bet:
    race = True
while race:
    for turtle in turtles:
        if turtle.xcor() > 290:
            race = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_turtle} turtle is the winner."
                      f"")
        rand_distance = r.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
