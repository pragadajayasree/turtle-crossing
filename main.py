import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()

    for i in car.all_cars:
        if player.distance(i) < 26:
            game_is_on = False
            level.over()

    if player.is_reached():
        player.reposition()
        car.level_up()
        level.inc()






screen.exitonclick()

