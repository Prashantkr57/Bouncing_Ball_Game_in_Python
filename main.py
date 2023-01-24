import time
from turtle import Turtle, Screen
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("BOUNCING BALL")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)
scoreboard = Scoreboard()

ball = Ball()


def move_left():
    paddle.backward(30)


def move_right():
    paddle.forward(30)


screen.listen()
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 275:
        ball.bounce_vertical()
    elif ball.xcor() > 275 or ball.xcor() < - 275:
        ball.bounce_horizontal()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_vertical()
        scoreboard.add_score()

    # Detect collision with the bottom wall
    if ball.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
