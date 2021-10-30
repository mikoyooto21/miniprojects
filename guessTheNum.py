import random

num = random.randint(1,10)
'''amount of chances'''
for i in range (0,3):   
	guess = int(input('Guess the number '))
	if guess == num:
		print(f"Amazing...\nYou guessed the number right! It's {num}")
		break
if guess != num:
	print(f"Your guess is incorrect. The number is {num}")