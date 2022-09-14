from turtle import Screen
import time
from snake import Snake
from food import Food
from scorecard import ScoreCard

# Set up the screen and heading
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="Exciting Snake Game")
screen.tracer(0)


game_on = True

snake = Snake()
food = Food()
scorecard = ScoreCard()

screen.listen()
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with Snake
    if snake.segments[0].distance(food) < 12:
        food.refresh()
        snake.extend()
        scorecard.update_score()

    # detect collision with wall:

    if snake.segments[0].xcor() > 285 or snake.segments[0].xcor() < -285 or snake.segments[0].ycor() > 285 \
            or snake.segments[0].ycor() < -285:
        game_on = False
        scorecard.game_over()

    # detect  collision with the body

    for segment in snake.segments:
        if snake.segments[0] == segment:
            pass
        elif snake.segments[0].distance(segment) < 10:
            game_on = False
            scorecard.game_over()








screen.exitonclick()
