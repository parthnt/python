from turtle import Turtle, Screen

timmy = Turtle()
new_screen = Screen()
timmy.color("pink")
timmy.begin_fill()
timmy.left(140)
timmy.forward(180)
timmy.circle(-90, 190)
timmy.left(100)
timmy.circle(-90, 190)

timmy.end_fill()

print(timmy.position())

new_screen.exitonclick()