# Tic Tac Toe, ou jeu du morpion

import random

def drawBoard(board):
	'''prints the board that it was passed. Board is a list of 10 strings representing the board (ignoring index 0)'''
	sep = '-----------'
	print('   |   |')
	print(' '+board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print(sep)
	print('   |   |')
	print(' '+board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print(sep)
	print('   |   |')
	print(' '+board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')

def inputPlayerLetter():
	'''Lets the player type the symbol they want.
	retuns a list with the player's letter as the first item, and the computer item as the secon'''
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print("Do you want to be X or O?")
		letter =input().upper()

	# the first item of the returned list is the players letter. If he inputs X, return [X, O], otherwise, return [O, X]
	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']

def whoGoesFirst():
	'''randomly chooses who goes first'''
	if random.randint(0,1) == 0:
		return 'computer'
	else:
		return 'player'

def playAgain():
	'''This function returns True if the player wants to play again, otherwhise it returns False'''
	print("Do you want to play again? (yes or no)")
	return input().lower().startswith('y')

def makeMove(board, letter, move):
	board[move] = letter

def isWinner(bo, le):
	'''given a board and the player's letter, returns True if the player as won'''
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or # check top line
	(bo[4] == le and bo[5] == le and bo[6] == le) or # check middle line
	(bo[1] == le and bo[2] == le and bo[3] == le) or # check bottom line
	(bo[1] == le and bo[4] == le and bo[7] == le) or # check left row
	(bo[2] == le and bo[5] == le and bo[8] == le) or # check middle row
	(bo[3] == le and bo[6] == le and bo[9] == le) or # check right row
	(bo[1] == le and bo[5] == le and bo[9] == le) or # check one diagonal
	(bo[3] == le and bo[5] == le and bo[7] == le))  # check other diagonal

def getBoardCopy(board):
	'''Makes a duplicate of the board list and returns the duplicate'''
	dupeBoard = []

	for i in board:
		dupeBoard.append(i)
	
	return dupeBoard

def isSpaceFree(board, move):
	'''Returns True if the passed move is free on the passed board'''
	return board[move] == ' '

def getPlayerMove(board):
	'''Lets the player type in his move'''
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print('What is your next move? (1-9)')
		move = input()
	return int(move)

def chooseRandomMoveFromList (board, movesList):
	'''Returns a valid move from the passed list on the passed board.
	Returns None if there is no valid move'''
	possibleMoves = []
	for i in movesList:
		if isSpaceFree (board, i):
			possibleMoves.append(i)

		if len(possibleMoves) != 0:
			return random.choice(possibleMoves)
		else:
			return None

def getComputerMove(board, computerLetter):
	'''given a board and the computer's letter, determine where to move and return that move'''
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	# algorith for the tic-tac-toe AI
	# first, check if it can win with the next move
	for i in range (1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy, computerLetter):
				return i
	# secondly, check if the next players move might make them win, and return a move that prevents it
	for i in range (1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i)
			if isWinner(copy, playerLetter):
				return i
	# third, try to take one of the corners, if any is free
	move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
	if move != None:
		return move

	# forth, try to take the center, if it is free
	if isSpaceFree(board, 5):
		return 5
	# fifth, make a move on one of the sides
	return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
	'''Returns True if every space on the passed board has been taken.
	Otherwise, returns False'''
	for i in range (1, 10):
		if isSpaceFree(board, i):
			return False
	return True

### begin
print ('Welcome to Tic-Tac-Toe!')

while True:
	# reset the board
	theBoard = [' '] * 10
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()
	print('The ' + turn + ' will go first.')
	gameIsPlaying = True

	while gameIsPlaying:
		if turn == 'player': # player's turn
			drawBoard(theBoard)
			move = getPlayerMove(theBoard)
			makeMove(theBoard, playerLetter, move)

			if isWinner(theBoard, playerLetter):
				drawBoard(theBoard)
				print('Congratulations! A winner is you!')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('Boo, the game is a tie…')
					break
				else:
					turn = 'computer'

		else: # computer's turn
			move = getComputerMove(theBoard, computerLetter)
			makeMove(theBoard, computerLetter, move)
			if isWinner(theBoard, computerLetter):
				drawBoard(theBoard)
				print('You loose!')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('Boo, the game is a tie…')
					break
				else:
					turn = 'player'
	if not playAgain():
		break

