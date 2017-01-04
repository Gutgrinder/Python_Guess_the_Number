import random


#input number
#check if it really is a number
#generate random number
#is number Higher or lower then random number?

print('''
Guess the Number
by Gerrit Ohrner
''')

maxZahl = input('In which range do you want to guess the number? (1-...): ')
while maxZahl.isdigit() == False:
	print('It must be a positiv number! ')
	maxZahl = input('In which range do you want to guess the number? (1-...): ')
maxZahl = int(maxZahl)
num = random.randint(1, int(maxZahl))
count = 0
print('Guess a number between 1 and', maxZahl)
guess = input()
while guess.isdigit() == False:
	print('It must be a positiv number! ')
	print('Guess a number between 1 and', maxZahl)
	guess = input()
guess = int(guess)
while guess != num:
	if guess < num:
		print('The number is to small')
		count = count + 1
		guess = int(input('Guess again: '))
	elif guess > num:
		print('The number is to big')
		count = count + 1
		guess = int(input('Guess again: '))
print('Congratulations, you guessed correct! You needed ', count, ' tries to succeed')
