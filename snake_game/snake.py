from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]


class Snake:
    def __init__(self):
        self.x_cord = 0
        self.segments = []
        self.create_snake()

    def add_segments(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.pensize(20)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for block in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[block - 1].xcor()
            new_y = self.segments[block - 1].ycor()
            self.segments[block].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

