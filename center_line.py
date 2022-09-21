from turtle import Turtle

class Line(Turtle):
    # Create initializer for center dashed line
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -300)
        self.color("white")
        self.hideturtle()
        for _ in range(0, 100):
            self.seth(90)
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)


