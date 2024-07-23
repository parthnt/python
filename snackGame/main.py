from turtle import Turtle, Screen
from snack import Snack
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0)
screen.listen()

snack = Snack()
screen.onkey(snack.up, "Up")
screen.onkey(snack.down, "Down")
screen.onkey(snack.right, "Right")
screen.onkey(snack.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snack.move()


screen.exitonclick()