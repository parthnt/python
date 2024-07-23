from turtle import Turtle, Screen, TK
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = True

def number_of_user():
    try:
        num = screen.textinput(title="Player's Count", prompt="How many players are going to play? : ")
        num = int(num)
        return num
    except ValueError:
        number_of_user()

def names_of_players(number, colors):
    players_list = []
    players_dir = {}
    for i in range(number):
        player_name = screen.textinput(title="player names", prompt="What do we call you? : ")
        players_list.append(player_name)
        players_dir[f"{colors[i]}"] = player_name
    return players_list, players_dir

def create_turtle(num):
    y_positions = [-70, -40, -10, 20, 50, 80]
    all_turtles = []
    for j in range(num):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[j])
        new_turtle.goto(x=-230, y=y_positions[j])
        all_turtles.append(new_turtle)
    return all_turtles

def get_locations(y):
    return y + 30


def restart():
    bool_value = int(screen.textinput(title="restart game", prompt="do still want to play this game? : "))
    if bool_value == 1:
        return True
    else: 
        return False

players = number_of_user()

players_list = names_of_players(players, colors)

turtles = create_turtle(players)


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = players_list[1][f"{turtle.pencolor()}"]            
            TK.messagebox.showinfo(title="The Turtle says:", message=f"The {winning_color} turtle is the winner!")
            is_race_on = restart()
            if is_race_on:

                screen.reset()
                turtles = create_turtle(players)
                break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)