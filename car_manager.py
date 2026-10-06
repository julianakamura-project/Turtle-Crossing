import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def create_car(self):
        dice = random.randint(1,6)
        if dice == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=320, y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT