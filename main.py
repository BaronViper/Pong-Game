from turtle import Screen
from pong import Pong
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
user_pong = Pong(positionx=350, positiony=0)
computer_pong = Pong(positionx=-350, positiony=0)

scoreboard = Scoreboard()
ball = Ball()

screen.onkeypress(user_pong.move_up, "Up")
screen.onkeypress(user_pong.move_down, "Down")
screen.onkeypress(computer_pong.move_up, "w")
screen.onkeypress(computer_pong.move_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(user_pong) < 50 and ball.xcor() > 320 or ball.distance(computer_pong) < 50 and ball.xcor() < -320:
        ball.collide()

    if ball.xcor() < -400:
        ball.original()
        scoreboard.r_score()

    if ball.xcor() > 400:
        ball.original()
        scoreboard.l_score()
    scoreboard.update()

screen.exitonclick()
