from turtle import Turtle
import random
import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

turtle.colormode(255)


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.red = random.randint(0, 255)
        self.green = random.randint(0, 255)
        self.blue = random.randint(0, 255)

    def create_snake(self):
        # Create Snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        timmy = Turtle("square")
        timmy.color(self.randomize_snake_color())
        timmy.penup()
        timmy.goto(position)
        self.segments.append(timmy)

    def extend(self):
        # add new segment to state
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        # self.segments[0].left(10)

    def randomize_snake_color(self):
        self.red = random.randint(0, 255)
        self.green = random.randint(0, 255)
        self.blue = random.randint(0, 255)
        col_combination = (self.red, self.green, self.blue)
        return col_combination

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
