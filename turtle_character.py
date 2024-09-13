from turtle import Turtle, Screen
rep = 25
screen = Screen()
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.setheading(90)
        self.reset_pos()
        self.shape("turtle")
        self.moving_up = False
        self.moving_down = False


    def move_up(self):
        if self.moving_up:
            new_y = self.ycor() + 20
            self.goto(self.xcor(),new_y)
            screen.ontimer(self.move_up, rep)  # Repeat every 25ms
            print("Moving up")

    def move_down(self):
        if self.moving_down:
            new_y = self.ycor() - 20
            self.goto(self.xcor(),new_y)
            screen.ontimer(self.move_down, rep) # Repeat every 25ms
            print("Moving down")

    def start_moving_up (self):
        self.moving_up = True
        self.move_up()
    def stop_moving_up(self):
        self.moving_up = False

    def start_moving_down(self):
        self.moving_down = True
        self.move_down()
    def stop_moving_down(self):
        self.moving_down = False

    def listen_keys(self):
        screen.listen()
        screen.onkeypress(self.start_moving_up, "w")
        screen.onkeypress(self.start_moving_down, "s")
        screen.onkeyrelease(self.stop_moving_up, "w")
        screen.onkeyrelease(self.stop_moving_down, "s")

    def reset_pos(self):
        self.clear()
        self.goto(0,-260)