import time
from turtle import Screen

import car_manager
import scoreboard
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

## Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Turtle Crossing")

## Components
turtle = Player()
cars = CarManager()
score = Scoreboard()

## Movements
screen.onkey(key="Up", fun=turtle.move_forward)
screen.onkey(key="Down", fun=turtle.move_backward)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    ### Car creation
    cars.create_car()
    cars.move()

    ### Level completion
    if turtle.ycor() > 280:
        #refresh, increase score and speed
        cars.increase_speed()
        score.increase_level()
        turtle.refresh()

    ### Collision with car
    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            score.game_over()
            game_is_on = False







screen.exitonclick()