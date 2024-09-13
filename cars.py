from turtle import Turtle, Screen
import random as rd 
screen = Screen()

class Cars(Turtle):
    def __init__(self, speed): 
        super().__init__()
        screen.colormode(255)
        self.color(self.random_colors())
        self.penup()
        self.shape("square")
        self.shapesize(1,2,0)
        self.setheading(180)
        self.setx(290)
        self.sety(rd.randint(-250, 260))
        self.move_speed = speed  # Use the passed speed
    def random_colors(self):
        r = rd.randint(0, 255)
        g = rd.randint(0, 255)
        b = rd.randint(0, 255)
        rgb = (r,g,b)
        return rgb
    
    def move_car(self, car):
        new_x = self.xcor()-self.move_speed
        car.goto(new_x, self.ycor())

    def detect_collision(self, car, player):
        # Define collision boundary for both car and player (assume both are square/rectangular)
        car_width = 40  # Approximate car width
        car_height = 20  # Approximate car height
        player_width = 20  # Approximate player width
        player_height = 20  # Approximate player height

        # Check for overlap between car and player bounding boxes
        if (player.xcor() - player_width/2 < car.xcor() + car_width/2 and
            player.xcor() + player_width/2 > car.xcor() - car_width/2 and
            player.ycor() - player_height/2 < car.ycor() + car_height/2 and
            player.ycor() + player_height/2 > car.ycor() - car_height/2):
            return True
        return False
