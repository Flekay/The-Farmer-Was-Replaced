# Returns the sign of a number.
#
# Arguments:
#	number (number): the number to get the sign of
#
# Returns:
#	number: 1 if positive, -1 if negative, 0 if zero
#
# Example:
#	sign(5)
#	# 1
#	sign(-3)
#	# -1
#	sign(0)
#	# 0
def sign(number):
	return (number > 0) - (number < 0)
