# The root function calculates the nth root of a number.
#
# Arguments:
#	number (number): the number to calculate the nth root of
#	n (number): the root to calculate
#
# Returns:
#	number: the nth root of the number
#
# Example:
#	root(8, 3)
#	# 2.0
def root(number, n):
	return number ** (1 / n)
