import random
while True:
	print('1. Roll the dice \n2. Exit')
	toDo = int(input('What you want to do?\n'))
	if toDo == 1:
		num = random.randint(1,6)
		print(f'Your number is: {num}\n')
	else:
		break