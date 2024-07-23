import random

def check_blank(list):
   for i in list:
      if i:
         continue
      else:
         return True

def printState(guesses):
	if guesses == 0:
		print(r"________      ")
		print(r"|      |      ")
		print(r"|             ")
		print(r"|             ")
		print(r"|             ")
		print(r"|             ")
	elif guesses == 1:
		print(r"________      ")
		print(r"|      |      ")
		print(r"|      0      ")
		print(r"|             ")
		print(r"|             ")
		print(r"|             ")
	elif guesses == 2:
		print(r"________      ")
		print(r"|      |      ")
		print(r"|      0      ")
		print(r"|     /       ")
		print(r"|             ")
		print(r"|             ")
	elif guesses == 3:
		print(r"________      ")
		print(r"|      |      ")
		print(r"|      0      ")
		print(r"|     /|      ")
		print(r"|             ")
		print(r"|             ")
	elif guesses == 4:
		print(r"________      ")
		print(r"|      |      ")
		print(r"|      0      ")
		print(r"|     /|\     ")  # Raw string
		print(r"|             ")
		print(r"|             ")
	elif guesses == 5:
		print(r"________      ")
		print(r"|      |      ")
		print(r"|      0      ")
		print(r"|     /|\     ")  # Raw string
		print(r"|     /       ")
		print(r"|             ")
	else:
		print(r"________      ")
		print(r"|      |      ")
		print(r"|      0      ")
		print(r"|     /|\     ")  # Raw string
		print(r"|     / \     ")  # Raw string
		print(r"|             ")


word_list = ["helo", "god", "wolf"]

word = random.choice(word_list)

num_word = len(word)

blank = []

for i in range(num_word):
   blank.append('')

print(blank)

isBlank = check_blank(blank)

guess_count = 0

while isBlank:
   char_guessed = input("guesse the charcter : ")

   splitted_word = list(word)

   for index, item in enumerate(splitted_word):
      if item == char_guessed:
         blank[index] = item
         print(blank)
         isBlank = check_blank(blank)
         if not isBlank:
            print("You have won this game")
         break
      else:
         if len(word) == index + 1:
            guess_count += 1
            printState(guess_count)
            if guess_count == 6:
                 print("You have lost this game")
                 isBlank = False
                 break
         continue