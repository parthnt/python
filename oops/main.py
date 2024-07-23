# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.name = username
#         self.following = 0
#         self.followers = 0
#
#     def follow(self, user):
#         self.following += 1
#         user.followers += 1
#
#
# user_1 = User("1", "parth")
# user_2 = User("2", "devansh")
# user_3 = User("3", "Abhay")
#
# user_1.follow(user_2)
#
# print(user_1.followers)
# print(user_1.following)

import random
from data import question_data
from qustion_modal import Question

first = random.choice(question_data)

question = Question(first["question"], first["correct_answer"])

print(question)