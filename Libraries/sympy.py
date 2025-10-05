help        = "https://github.com/Flekay/The-Farmer-Was-Replaced/tree/main/general/sympy"
constants   = "[]"
functions   = "[fibonacci, isprime, nextprime, prevprime, primerange]"

# Fibonacci numbers using Binet's formula
#
# Arguments:
#	n (int): the index of the Fibonacci number to compute
# Returns:
#	int: the nth Fibonacci number
# Example:
#	nth_fibonacci = fibonacci(10)
#	# print(nth_fibonacci)  # Output: 55
_sqrt5 = 5 ** 0.5
_phi = (1 + _sqrt5) / 2
_phi1 = 1 - _phi
def fibonacci(n):
	return (_phi ** n - _phi1 ** n) / _sqrt5

# Check if a given number is a prime number.
#
# Arguments:
#	n (int): the number to check
#
# Returns:
#	bool: True if the number is prime, False otherwise
#
# Example 1:
#	isprime(97)
#	# True
def isprime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	p = 3
	sqrt = n**0.5
	while p <= sqrt:
		if n % p == 0:
			return False
		p += 2
	return True

# Get the next prime number after a given number.
#
# Arguments:
#	n (int): the number to start from
#
# Returns:
#	int: the next prime number
#
# Example 1:
#	nextprime(97)
#	# 101
def nextprime(n):
	candidate = n + 1
	if candidate < 2:
		candidate = 2
	if candidate == 2:
		return 2
	if candidate % 2 == 0:
		candidate += 1
	while True:
		limit = candidate**0.5 + 1
		is_prime = True
		for d in range(3, limit, 2):
			if candidate % d == 0:
				is_prime = False
				break
		if is_prime:
			return candidate
		candidate += 2

# Get the previous prime number before a given number.
#
# Arguments:
#	n (int): the number to start from
#
# Returns:
#	int: the previous prime number
#
# Example 1:
#	prevprime(97)
#	# 89
def prevprime(n):
	candidate = n - 1
	while candidate >= 2:
		if candidate == 2:
			return 2
		if candidate % 2 == 0:
			candidate -= 1
			continue
		limit = candidate**0.5 + 1
		is_prime = True
		for d in range(3, limit, 2):
			if candidate % d == 0:
				is_prime = False
				break
		if is_prime:
			return candidate
		candidate -= 2
	return None

# Get a list of prime numbers in a given range.
#
# Arguments:
#	a (int): the start of the range
#	b (int): the end of the range
#
# Returns:
#	list: the list of prime numbers in the range
#
# Example 1:
#	primerange(10, 20)
#	# [11, 13, 17, 19]
def primerange(a, b):
	if a > b or b < 2:
		return []
	bp1 = b + 1

	sieve = [False, False]
	for i in range(1, b):
		sieve.append(True)

	for p in range(2, b**0.5 + 1):
		if sieve[p]:
			for i in range(p * p, bp1, p):
				sieve[i] = False

	primes = []
	for n in range(a, bp1):
		if sieve[n]:
			primes.append(n)
	return primes

