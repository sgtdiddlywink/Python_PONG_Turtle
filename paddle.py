from turtle import Turtle


# Create initial class for paddle
class Paddle(Turtle):

    # Code to determine what happens when we initialize a new paddle object. This is to be applied with every new object
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        
    # Create method for moving paddle upwards
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Create method for moving paddle down
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
