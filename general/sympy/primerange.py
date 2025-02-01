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
