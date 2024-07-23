from turtle import Turtle, Screen
import random

user = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
players = screen.textinput(title="How many players are there", prompt="How many players are there : ")
players = int(players)
y_positions = [-70, -40, -10, 20, 50, 80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
players_names = []
is_race_on = True
for index in range(0, players):
    player_name = screen.textinput(title="Enter a name", prompt="please enter player names: ")
    players_names.append(player_name)

all_turtles = []

i = 0
player_dir = {}


def reset_turtle_location(turtles, y_position):
    for j, item in enumerate(turtles):
        print(item)
        item.goto(x=-230, y=y_position[j])


for index_number in players_names:
    player_dir[f"{colors[i]}"] = f"{index_number}"
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)
    i += 1

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            # is_race_on = False
            winning_color = turtle.pencolor()
            print(f"{player_dir[winning_color]} have won the match")
            restart_game = screen.textinput(title="restart game?? ", prompt="restart game??")
            if restart_game == 1:
                reset_turtle_location(all_turtles, y_positions)
                is_race_on = True
            else:
                is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()