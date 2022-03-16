from turtle import *
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle(370, 0)
l_paddle = Paddle(-375, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_Speed)
    screen.update()
    ball.move()

    # Detect collision with the upper and lower wall
    if ball.ycor() > 279 or ball.ycor() < -279:
        ball.bounce_y()

     # Detect collision with paddle
    elif ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -315:
        ball.bounce_x()

    # Detect collision with the right
    elif ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()

    # Detect collision with left wall
    elif ball.xcor() < -385:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
