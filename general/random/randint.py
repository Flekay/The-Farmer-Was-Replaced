# Returns a random integer between two given integers.
#
# Arguments:
#	a (int): the lower bound of the random integer
#	b (int): the upper bound of the random integer
#
# Returns:
#	int: a random integer between a and b
#
# Example 1:
#	randint(1, 10)
#	# 7
def randint(a, b):
	return (random() * (b - a + 1) + a) // 1
