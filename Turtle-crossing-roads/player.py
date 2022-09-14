from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINAL_Y_CORD = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def has_reached_destination(self):
        """Returns True if the tutle has crossed the road successfully"""
        return self.ycor() >= FINAL_Y_CORD

    def player_reposition(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

