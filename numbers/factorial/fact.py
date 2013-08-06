# fonctions pour manipuler des factorielles de nombres entiers et positifs.
# rappel : factorielle n = n * (n - 1) * (n - 2) ... * 2 * 1
def fact(n):
	'''takes a positive integer as argument. Returns its factorial'''
	n = abs(int(n))
	facto = 1
	if n == 0:
		return 0
	for i in range(1, n + 1):
		facto = facto * i
	return facto

def list_fact(n):
	'''retourne une liste des factorielles de 1 à n'''
	list = []
	n = abs(int(n))
	calcul = 1
	
	for i in range(1, n + 1):
		calcul *= i
		list.append(calcul)

	return list

def dict_fact(n):
	'''retourne un dictionnaire avec de 1 à n et de 1! à n! comme clé et valeur'''
	dict = {}
	n = abs(int(n))
	calcul = 1
	s = ''	
	for i in range(1, n + 1):
		calcul *= i
		dict.update({i:calcul})

	return dict
if __name__ == '__main__':
	print('1! =',fact(1))
	print('2! =',fact(2))
	print('3! =',fact(3))
	print('4! =',fact(4))
	print('5! =',fact(5))
