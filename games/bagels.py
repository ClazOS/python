# Jeu du bagels.
# Un joueur pense à un nombre à plusieurs chiffres sans répétition de chiffres, 123 et pas 121 par exemple
# L’autre joueur essaie de deviner ce nombre et fait des propositions.
# Pour l’aider, le premier joueur lui dit :
# bagels si le nombre proposé n’a aucun chiffre en commun avec la solution
# pico pour chaque chiffre proposé dans la solution mais à une mauvaise place
# fermi pour chaque chiffre proposé dans la solution et à la bonne place.

import random
def getSecretNum(numDigits):
	'''Returns a string that is numDigits long, made up of unique random digits.'''
	numbers = list(range(10))
	random.shuffle(numbers)
	secretNum = ''
	for i in range(numDigits):
		secretNum += str(numbers[i])
	return secretNum

def getClues(guess, secretNum):
	'''Returns a string with the pico, fermi, bagels clues to the user.'''
	if guess == secretNum:
		return 'A winner is you!'
	
	clue = []

	for i in range (len(guess)):
		if guess[i] == secretNum[i]:
			clue.append('Fermi')
		elif guess[i] in secretNum:
			clue.append('Pico')
	
	if len(clue) == 0:
		return 'Bagels'

	clue.sort()
	return ' '.join(clue)

def isOnlyDigits(num):
	'''Returns True if num is a string made up only of digits. Otherwise, returns False'''
	if num == '':
		return False

	for i in num:
		if i not in '0 1 2 3 4 5 6 7 8 9'.split():
			return False
		return True
def playAgain():
	print('Do you want to play again, buddy? ([y]es or [n]o)')
	return input().lower().startswith('y')

#begin

NUMDIGITS = 3
MAXGUESS = 10

print ('I am thinking of a %s-digit number. Try to guess what it is.' %(NUMDIGITS))
print('Here are some clues:')
print('When I say: \t That means:')
print('Pico \t \t One digit is correct but in the wrong position.')
print('Fermi \t \t One digit is correct and in the right position.')
print('Bagels \t \t No digit is correct.')

while True:
	secretNum = getSecretNum(NUMDIGITS)
	print('I have though up a number. You have %s guesses to get it.'%(MAXGUESS))

	numGuesses = 1
	while numGuesses <= MAXGUESS:
		guess = ''
		while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
			print('Guess #%s: ' % (numGuesses))
			guess = input()

		clue = getClues(guess, secretNum)
		print(clue)
		numGuesses += 1

		if guess == secretNum:
			break
		if numGuesses > MAXGUESS:
			print('You ran out of guesses. The answer was %s.' %(secretNum))
	
	if not playAgain():
		break
