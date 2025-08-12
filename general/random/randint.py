# Returns a random integer between two given integers.
#
# Arguments:
#	low (int): the lower bound of the random integer
#	high (int): the upper bound of the random integer
#
# Returns:
#	int: a random integer between low and high
#
# Example 1:
#	randint(1, 10)
#	# 7
def randint(low, high):
	return (random() * (high - low + 1) + low) // 1
