from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.show_score()

    def update_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-240, 280)
        self.write(arg=f"Level: {self.score}", align="left", font=("arial", 10, "bold"))

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(arg="Game Over", align="Center", font=("arial", 10, "bold"))


