# Divides two numbers and returns the quotient and remainder.
#
# Arguments:
#	dividend (number): the number to be divided
#	divisor (number): the number to divide by
#
# Returns:
#	tuple: a tuple containing the quotient and remainder
#
# Example:
#	divmod(17, 10)
#	# (1, 7)
def divmod(dividend, divisor):
	return (dividend // divisor, dividend % divisor)
