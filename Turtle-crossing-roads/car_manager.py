from turtle import Turtle
import random
import time

CAR_COLORS = ("red", "green", "blue", "yellow", "orange", "brown", "crimson")
X_AXIS_BORDER = 290
Y_AXIS_BORDER = 250
INITIAL_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()

        self.car_speed = INITIAL_MOVE_DISTANCE
        self.all_cars = []
        self.sleep = 0.5
        self.hideturtle()

    def manage_cars(self):
        # for _ in range(21):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            random_color = random.choice(CAR_COLORS)
            car = Turtle()
            car.shape("square")
            car.color(random_color)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            # random_x_cor = random.randint(-1 * X_AXIS_BORDER, X_AXIS_BORDER)
            random_y_cor = random.randint(-1 * Y_AXIS_BORDER, Y_AXIS_BORDER)
            car.goto(300, random_y_cor)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            # car.setheading(270)
            car.backward(self.car_speed)
            # if car.xcor() <= -1 * X_AXIS_BORDER:
            #     random_y_cor = random.randint(-1 * Y_AXIS_BORDER, Y_AXIS_BORDER)
            #     car.goto(X_AXIS_BORDER, random_y_cor)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT






