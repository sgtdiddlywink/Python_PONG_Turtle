from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    # Create initializer for Scoreboard class
    def __init__(self, position):
        # We want the Scoreboard class to inherit attributes from super Turtle class
        super().__init__()
        self.goto(position)
        # Utilize write to put scoreboard up
        self.score = 0
        self.color("white")
        self.penup()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    # Method to update the scoreboard
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    # Method to increase score on scoreboard
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
