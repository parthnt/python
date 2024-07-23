from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0)
starting_position = [(0, 0), (-20, 0), (-40, 0)]
move = []

for index in starting_position:
    snack = Turtle(shape="square")
    snack.penup()
    snack.color("white")
    snack.goto(index)
    move.append(snack)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for num in range(len(move) - 1, 0, -1):
        new_x = move[num - 1].xcor()
        new_y = move[num - 1].ycor()
        move[num].goto(new_x, new_y)
    move[0].forward(20)
    move[0].left(90)


screen.exitonclick()