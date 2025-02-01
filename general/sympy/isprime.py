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
