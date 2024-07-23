import colorgram
from turtle import Turtle, Screen

# Extract 6 colors from an image.
colors = colorgram.extract('images.png', 121)

first_color = colors[0]
rgb = first_color.rgb
hsl = first_color.hsl
proportion = first_color.proportion

turtle = Turtle()
new_screen = Screen()

new_screen.colormode(1)

i = 1
turtle.setheading(225)
turtle.penup()
turtle.forward(300)
turtle.setheading(0)

for color in colors:
    # turtle.pendown()
    r = color.rgb.r / 255
    g = color.rgb.g / 255
    b = color.rgb.b / 255
    turtle.dot(20,(r, g, b))
    turtle.forward(10)
    turtle.pencolor(r, g, b)
    turtle.pensize(10)
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    if i % 5 == 0:
        # turtle.pendown()
        turtle.left(90)
        turtle.forward(30)
        turtle.setheading(180)
        turtle.forward(150)
        turtle.setheading(0)

    i += 1

new_screen.exitonclick()

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s
