from turtle import Turtle
SEGMENT_POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snack:

    def __init__(self):
        self.segment = []
        self.create_snack()
        self.head = self.segment[0]

    def create_snack(self):
        for index in SEGMENT_POSITION:
            snack = Turtle(shape="square")
            snack.penup()
            snack.color("white")
            snack.goto(index)
            self.segment.append(snack)

    def move(self):
        for num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[num - 1].xcor()
            new_y = self.segment[num - 1].ycor()
            self.segment[num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)