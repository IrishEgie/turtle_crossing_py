from turtle import Turtle

FONT = ('Courier', 10, 'bold')

class LevelIndicator(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = -1
        self.goto(-250, 260)
        self.write_level()
        print("Level is printed")

    def write_level(self):
        self.clear()
        self.level +=1
        self.write(f"Level: {self.level}", move=False, align='center', font=FONT)
        return self.level
        
