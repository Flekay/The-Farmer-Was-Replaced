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
