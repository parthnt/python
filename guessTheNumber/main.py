import random

a = -1
n = random.randint(1, 100)
g = 0

while(a != n):
   g += 1
   a = int(input("Guess the number: "))
   if(a < n):
      print("Too low")
   elif(a > n):
      print("Too high")


print(f"Guess currect in {g} number of try")