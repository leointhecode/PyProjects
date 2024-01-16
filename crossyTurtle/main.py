from turtle import Screen
from roadTurtle import RoadTurtle
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("crossyTurtle")
screen.tracer(0)

cTurtle = RoadTurtle()
car = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(cTurtle.move, "Up")

chance = 6
game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)

    car.more_cars(scoreboard.level, chance)

    for n in car.cars:
        n.move()

    if cTurtle.ycor() > 250:
        cTurtle.goto((0, -270))
        chance += 1
        scoreboard.new_level()

    for kill_car in car.cars:
        if cTurtle.distance(kill_car) < 15:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()
