from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

U_WALL = 290
D_WALL = -290
R_WALL = 400
L_WALL = -400

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PyPong")
screen.tracer(0)

user = Paddle((-350, 0))
adv = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(adv.up, "Up")
screen.onkeypress(adv.down, "Down")
screen.onkeypress(user.up, "w")
screen.onkeypress(user.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)

    ball.move()

    if ball.distance(x=adv.xcor(), y=adv.ycor() + 30) < 35 or ball.distance(x=adv.xcor(), y=adv.ycor() - 30) < 35 \
            or ball.distance(adv) < 35:
        ball.pad_bounce()
    if ball.distance(x=user.xcor(), y=user.ycor() + 30) < 35 or ball.distance(x=user.xcor(), y=user.ycor() - 30) < 35 \
            or ball.distance(user) < 35:
        ball.pad_bounce()
    if ball.ycor() > U_WALL or ball.ycor() < D_WALL:
        ball.wall_bounce()

    if ball.xcor() > R_WALL:
        score.user_point()
        score.count_score()
        ball.refresh()
    elif ball.xcor() < L_WALL:
        score.adv_point()
        score.count_score()
        ball.refresh()

screen.exitonclick()
