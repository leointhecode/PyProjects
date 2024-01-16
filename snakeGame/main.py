import time
import snake as s
import turtle as t
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My python game or was it a snake?...")
screen.tracer(0)

snake = s.Snake()
yummy_ball = Food()
board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    board.update_scoreboard()
    snake.move()

    if snake.head.distance(yummy_ball) < 15:
        yummy_ball.refresh()
        board.count_score()
        snake.add_segment()

    if snake.head.xcor() > 280 or snake.head.ycor() > 300 or snake.head.xcor() < -310 or snake.head.ycor() < -280:
        snake.reset()
        board.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            board.reset()
            snake.reset()
    board.new_high_score()

screen.exitonclick()
