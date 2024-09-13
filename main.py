from turtle import Screen
from turtle_character import Player
from cars import Cars
import time
import random as rd

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen_height = screen.window_height()/2
screen_width = screen.window_width()/2


player = Player()
game_is_on = True


# List to store car objects
car_list = []

while game_is_on:
    time.sleep(0.1)

    for i in range(rd.randint(1, 5)):
        if rd.randint(1,6) == 1:
            car = Cars()  # Create a new car object
            car_list.append(car)  # Append it to the list
        for car in car_list:
            car.move_car(car)
            if car.xcor() <= -screen_width-30:
                car_list.remove(car)
                print(" A car has been removed")

    screen.update()

screen.exitonclick()