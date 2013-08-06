# Fibonacci series:
# the sum of two elements defines the next

def fibo(n):
	'''takes a positive integer and returns the value of it's fibo'''
	a, b = 0, 1
	if n < 0:
		raise ValueError('number must a positive integer')
	if n  == 0:
		return a
	for i in range (1, n):
		a, b = b, a + b
	return b

def golden(m):
	'''takes a positive integer and gives approximation of the golden ratio of its order through fibo(m) / fibo(m-1)'''
	if m < 1:
		raise ValueError('number must an integer superior to zero')
	return fibo(m) / fibo(m-1)

def sfibo(k):
	'''takes a positive integer and prints the values of fibos up to it'''
	c, d = 0, 1
	if k < 0:
		raise ValueError('number must a positive integer')

	for j in range (0, k + 1):
		print('fibo(',j,') = ', c)
		c, d = d, c + d

if __name__=='__main__':
	sfibo(10)
