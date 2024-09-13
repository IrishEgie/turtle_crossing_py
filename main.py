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

cars_on_screen_threshold = 10
car_move_speed_increase = 1
car_move_speed = 2
while game_is_on:
    player.listen_keys()

    if rd.randint(1,20) == 1 and len(car_list) < cars_on_screen_threshold:
        car = Cars(speed=car_move_speed)  # Create a new car object
        car_list.append(car)  # Append it to the list
    for car in car_list:
        car.move_car(car)
        if car.xcor() <= -screen_width-30:
            car_list.remove(car)
            print(" A car has been removed")
        if car.detect_collision(car,player):
            print("Player Collision detected")
            game_is_on = False  # End game on collision (optional)
            lvl.write_end()

    # Check if the player reaches the top of the screen
    if player.ycor() >= screen_height + 20:
        # Level up the game
        lvl.write_level()
        player.reset_pos()

        car_move_speed += car_move_speed_increase


    time.sleep(0.01)
    screen.update()

screen.exitonclick()