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
