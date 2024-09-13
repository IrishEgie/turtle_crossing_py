from turtle import Screen
from turtle_character import Player
from cars import Cars
from level import LevelIndicator
import time
import random as rd

screen = Screen()

screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen_height = screen.window_height()/2
screen_width = screen.window_width()/2

lvl = LevelIndicator()
player = Player()
game_is_on = True


# List to store car objects
car_list = []

while game_is_on:
    player.listen_keys()

    for i in range(5):
        if rd.randint(1,6) == 1:
            car = Cars()  # Create a new car object
            car_list.append(car)  # Append it to the list
        for car in car_list:
            car.move_car(car)
            if car.xcor() <= -screen_width-30:
                car_list.remove(car)
                print(" A car has been removed")
    if player.ycor() >= screen_height+20:
        lvl.write_level()
        player.reset_pos()


    

    time.sleep(0.2)
    screen.update()

screen.exitonclick()