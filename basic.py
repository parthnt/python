#print("hello world")

#expor = 4 ** 4 # 4 * 4 * 4 * 4 = 256
#floor_division = 16 // 5 # return 3 as only int not the flort
#module = 7 % 3 # remender

# prority level -- jo tuje nai mili
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. <, >, <=, >=, !=, ==
# 6. and
# 7. or
# 8. not

# 15 / 3 * 2 * 2 - (3 + 4) 
# 15 / 3 * 2 * 2 - (7)
# 5 * 2 * 2 - 7
# 20 - 7
# 13

# number = 5
# number **= 3
# print(number) # 125

# loop
# for i in range(1, 11):
#     print(i)

# slice
# ex1 = "this is string"
# print(ex1[0:4]) 

#concadinate
# concadinate = "this " + "is " + "concadinate"
# print(concadinate)

# type function
# ex_1 = False
# ex_2 = 12
# ex_3 = "hello"
# ex_4 = 12.5
# print(type(ex_1))
# print(type(ex_2))
# print(type(ex_3))
# print(type(ex_4))

# convert to string
# ex2 = str(145)
# print(type(ex2))

# tab charcater \t for string
# print("this\tis\tnew\tstring")

# new line charcater \n
# print("this\nis\nin\nnew\nline")

# print("*******\n *****\n  ***\n   *")

# input funtion
#
# name = input("whats your name?? ")
# print("hello " + name)

# create function
#
# def functionName():
#    print(2+2)
#
# functionName()

# import module
#
# import random
# print(random.randint(1, 10))

# import module function
#
# from random import randint
# print(randint(1,100))

# local and global variable

# example = "this is global" # global variable
#
# def functionName():
#     example = "this is local" # local variable
#     return example
#
# print(example)
# print(functionName())

# if else statements
# veg = input("any vegetable name? ")
#
# if veg == "cron":
#     print("vegetable is cron")
# elif veg == "tame-to":
#     print("tame-to")
# else:
#     print("vegetable is different")

# counter = 10
#
# while counter >= 0:
#     print(counter)
#     counter -= 1

# for loop
#
# word = "home"
#
# for letter in word:
#     print(letter)

# user_str = "Please enter a string."
#
# count = 0
# for char in user_str:
#     count += 1
#
# print(user_str)
# print(count)

# one_input = range(5)
#
# for num in one_input:
#     print(num)

# two_input = range(4, 10)
# for numb in two_input:
#     print(numb)
#
# three_input = range(2, 12, 2)
# for numbs in three_input:
#     print(numbs)

# def factorial(fac_num):
#     returned = 1
#     for item in range(fac_num, 1, -1):
#         returned *= item
#     return returned
#
#
# print(factorial(3))  # 6
# print(factorial(4))  # 24
# print(factorial(5))  # 120

# format() function

# name = "parth"
# num = 10
#
# print("hyy {}, it {} o clock".format(name, num))

# list datatype

# example_one = ["hy", "true", 10]
#
# for str_ in example_one:
#     print(str_)

# example_one = ["hy", "true", 10]
# print(example_one)
# del example_one[2]
# print(example_one)
# example_one.remove("true")
# print(example_one)
# example_one.append("parth")
# print(example_one)
# example_one.insert(2, "new")
# print(example_one)

# num_list = [10, 15, 50, 4]
# num_list.sort(reverse=True)
# print(num_list)

# dictionaries
# con = {
#     "name":"Parth",
#     "study":"BCA"
# }

# tuple
# tuple_1 = (1, 2, 3)
# tuple_2 = tuple([2, 4, 5])
# tuple_3 = tuple("abcd")
#
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)

# import pyjokes
#
# joke = pyjokes.get_joke()
#
# print(joke)

# speak module
# import pyttsx3
# import pyjokes
#
# joke = pyjokes.get_joke()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# print(joke)
# engine.say(joke)
# engine.runAndWait()


# import os
#
# directoryPath = 'c:/xampp7.3'
#
# content = os.listdir(directoryPath)
#
# print(content)


# def factorial(n):
#     if(n == 1 or n == 0):
#         return 1
#     return n * factorial(n-1)
#
# a = int(input("enter a number "))
#
# print(factorial(a))

# def naturalNum(n):
#     if(n == 1):
#         return  1
#     return  naturalNum(n - 1) + n
#
# a = int(input("enter a number "))
#
# print(naturalNum(a))


# def pattern(n):
#     if(n == 1):
#         return "*"
#     print("*" * n)
#     return pattern(n-1)

# a = int(input("enter a number "))
# print(pattern(a))

# f = open("myFile.txt", "w")
# f.write("Hello World")
# f.close()

# f = open("myFile.txt")
# data = f.read()
# print(data)
# f.close()

# classes

# class Empoloyee:
#    language = "python"
#    salary = 12500

#    def __init__(self, name, age, gender):
#       print("this is dunder method")

#    def getinfo(self):
#       print("language is ", self.language)
#       print("salary is ", self.salary)
   
#    @staticmethod
#    def greet():
#       print("hello world")


# parth = Empoloyee()
# parth.language = "javascript"
# parth.getinfo()
# parth.greet()


# inheritance
# class parents:
#    a = "parents"

# class firstChild(parents):
#    b = "first child"

# class secondChild(firstChild):
#    c = "second child"


# o = secondChild

# print(o.b)

# class employee:
#    a= 10
#    @classmethod
#    def show(cls):
#       print(f"this is employee class attr {cls.a}")


# e = employee()
# e.a = 45
# e.show()


# class emloyee:
#    a= 10
#    @classmethod
#    def show(cls):
#       print(f"this is employee class attr {cls.a}")
#    @property
#    def name(self):
#       return self.name
   
#    @name.setter
#    def name(self, value):
#       self.fname = value

   
# e = emloyee()
# e.name = "parth"
# print(e.fname)
# e.show()


# class Number:
#    def __init__(self, n):
#       self.n = n

# a = Number(1)
# b = Number(2)
# print(a.n + b.n)

# declare variable type
# n : int = 5

# merge dicnory
# a = {"a":1 , "b" : 2}
# b = {"c":3 , "d" : 4}

# c = a | b
# print(c)

# exeption handling
# try:
#    a = int(input("enter a number : "))
#    print(a)
# except Exception as e:
#    print(e)
# finally:
#    print("this is finally block") # finally is statement that run every times even if its in function with return statment


# l = [0, 3, 4, 45, 54]
# index = 0
# for item in l:
#    print(f"in index of {index} value is {item}")
#    index += 1

# by using enumerate function

# for index, item in enumerate(l):
#    print(f"in index of {index} value is {item}")

# lambda
# def squer(x):
#    return x * x

# squer = lambda x : x * x 
# print(squer(5))


l = [0, 3, 4, 45, 54]

squer = lambda x : x * x 

sqlList = map(squer, l)
print(list(sqlList))