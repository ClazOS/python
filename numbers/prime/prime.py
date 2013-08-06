# functions dealing with prime numbers

def is_a_prime(n):
	''' takes a positive integer as argument. Returns True if it's a prime number, False if it's not a prime'''
	n = abs(int(n))
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	max = n**0.5 + 1
	i = 3

	while i <= max:
		if n % i == 0:
			return False
		i = i + 2
	return True

def list_primes(n):
	'''returns a list of the arg first prime numbers'''
	primes = []
	j = 0
	while len(primes) < n:
		j = j + 1
		if is_a_prime(j):
			primes.append(j)
	return primes


if __name__ == '__main__':
	print('The first ten prime numbers are', list_primes(10))
