from turtle import Screen
from player import Player
from car_manager import CarManager
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Road")
screen.tracer(0)

game_on = True

player = Player()
scoreboard = ScoreBoard()
cars = CarManager()
screen.listen()
screen.onkeypress(fun=player.move_player, key="Up")


while game_on:
    screen.update()
    time.sleep(0.1)
    cars.manage_cars()
    cars.move_cars()

    # Check if player has reached the destination
    if player.has_reached_destination():
        scoreboard.update_score()
        player.player_reposition()
        cars.increase_car_speed()

    # # Detect collision with the cars

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()







screen.exitonclick()