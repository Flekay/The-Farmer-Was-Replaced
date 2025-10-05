# Rounds a number up to the nearest integer.
#
# Arguments:
#	number (number): the number to round up
#
# Returns:
#	number: the rounded up number
#
# Example:
#	ceil(1.1)
#	# 2
def ceil(number):
	return -(-number // 1)
