from turtle import Turtle
import random

class Ball(Turtle):
    # Create initializer for Ball class
    def __init__(self):
        # We want the ball class to inherit attributes from super Turtle class
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        direction = random.choice([1, -1])
        self.x_move = 10 * direction
        self.y_move = 10 * direction

    # Create new method to move ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Create method for rebounding the ball of top and bottom
    def bounce_y(self):
        self.y_move *= -1

    # Create method for rebounding the ball of right paddle
    def bounce_r(self):
        self.x_move *= -1

    # Create method for rebounding the ball of left paddle
    def bounce_l(self):
        self.x_move *= -1

    # Create new method to refresh ball location
    def refresh(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1 * random.choice([1, -1])


