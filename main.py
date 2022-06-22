from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()

screen.setup(width=800, height=600)

screen.bgcolor("black")

screen.tracer(0)
scoreboard = Scoreboard()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
is_on = True
screen.listen()

while is_on:
    screen.update()
    screen.onkeypress(fun=r_paddle.move_up, key="Up")
    screen.onkeypress(fun=r_paddle.move_down, key="Down")
    screen.onkeypress(fun=l_paddle.move_up, key="w")
    screen.onkeypress(fun=l_paddle.move_down, key="s")
    time.sleep(0.07)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        ball.speed_up()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed_up()
    if ball.xcor() > 380:
        ball.setposition(0, 0)
        ball.bounce_x()
        ball.bounce_y()
        scoreboard.left_score_change()
        ball.slow_down()
    if ball.xcor() < -380:
        ball.setposition(0, 0)
        ball.bounce_x()
        ball.bounce_y()
        scoreboard.right_score_change()
        ball.slow_down()

screen.exitonclick()
