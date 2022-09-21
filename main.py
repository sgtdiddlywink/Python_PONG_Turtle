"""This code and project was part of Angela Yu's 100 Days of Code for Python.  I take no credit for it and am still learning."""

# Imports to be included as part of code
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from center_line import Line
import time

# Set up screen object from Screen Class
screen = Screen()
# Set screen dimensions
screen.setup(width=800, height=600)
# Change background color
screen.bgcolor("black")
# Set window title
screen.title("PONG")
screen.tracer(0)

# Create paddle objects from Paddle class
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create object for center line
line = Line()

# Create ball object from Ball class
ball = Ball()

# Create scoreboard from Scoreboard Class
scoreboard_l = Scoreboard((-200, 275))
scoreboard_r = Scoreboard((200, 275))

# Tell the screen to start listening for keystrokes
screen.listen()
# Keys to detect and the functions to bind them to
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball_time = .1
# While loop to move initial segments
game_is_on = True
while game_is_on:
    # Refresh screen
    time.sleep(ball_time)
    screen.update()
    ball.move()
    # Detect collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect when ball hits right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_r()
        ball_time *= .9

    # Detect when ball hits left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_l()
        ball_time *= .9

    # Detect when right paddle misses the ball
    if ball.xcor() > 390:
        ball.refresh()
        scoreboard_l.increase_score()
        ball_time = .1

    # Detect when left paddle misses the ball
    if ball.xcor() < -390:
        ball.refresh()
        scoreboard_r.increase_score()
        ball_time = .1

screen.exitonclick()
