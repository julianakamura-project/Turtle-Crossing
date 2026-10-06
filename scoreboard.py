from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 260)
        self.update_level()

    def update_level(self):
        self.write(
            arg=f"Level: {self.level}",
            move= False,
            align= ALIGNMENT,
            font= FONT
        )

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write(
            arg= "GAME OVER",
            move= False,
            align= "center",
            font= FONT
        )