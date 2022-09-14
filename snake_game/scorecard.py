from turtle import Turtle


class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(0, 280)
        self.show_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}", align="center", font="arial")

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font="arial")
