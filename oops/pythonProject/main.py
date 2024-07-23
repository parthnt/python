# from turtle import Turtle, Screen
#
# timmy = Turtle()
# new_screen = Screen()
# heart shape
# timmy.color("pink")
# timmy.begin_fill()
# timmy.left(140)
# timmy.forward(180)
# timmy.circle(-90, 190)
# timmy.left(100)
# timmy.circle(-90, 190)
#
# timmy.end_fill()

# square
# for _ in range(6):
#   timmy.forward(100)
#   timmy.left(60)
#
# new_screen.exitonclick()
# timmy.end_fill()


#
# timmy.speed("fastest")
# i = 10
# for _ in range(15):
#     for _ in range(35):
#         timmy.circle(80, 360)
#         timmy.left(i)
#     i = i + 2
#
# new_screen.exitonclick()

# from prettytable import from_csv

# import mysql.connector
# from prettytable import PrettyTable, from_db_cursor
#
# table = PrettyTable()
# table.align = "r"
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="sahjanand"
# )
#
# cursor = mydb.cursor()
#
# cursor.execute("SELECT * FROM question")
#
# table = from_db_cursor(cursor)
#
# print(table)


# with open("category.csv") as fp:
#     table = from_csv(fp)
# print(table)
# table = PrettyTable()
#
# table.add_column("pikachu names", ['pikachu', 'charmander'])
# table.add_column("type", ['lightning', 'fire'])
# print(table)

