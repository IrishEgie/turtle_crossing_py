from turtle import Turtle, Screen
import random as rd 
screen = Screen()

class Cars(Turtle):
    def __init__(self): 
        super().__init__()
        screen.colormode(255)
        self.color(self.random_colors())
        self.penup()
        self.shape("square")
        self.shapesize(1,3,1)
        self.setheading(180)
        self.speed(rd.randint(5,15))
        self.setx(290)
        self.sety(rd.randint(-275, 275))

    def random_colors(self):
        r = rd.randint(0, 255)
        g = rd.randint(0, 255)
        b = rd.randint(0, 255)
        rgb = (r,g,b)
        return rgb
    
    def move_car(self, car):
        new_x = self.xcor()-20
        car.goto(new_x, self.ycor())

 