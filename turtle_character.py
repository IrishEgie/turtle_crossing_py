from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(0,-260)
        self.shape("turtle")
