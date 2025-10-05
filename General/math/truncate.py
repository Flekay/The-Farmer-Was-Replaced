# Truncates a number to a specified number of decimal places.
#
# Arguments:
#	number (number): the number to truncate
#	decimals (int): the number of decimal places to truncate to (default is 0)
#
# Returns:
#	number: the truncated number
#
# Example 1:
#	truncate(1.123456789)
#	# 1
def truncate(number, decimals=0):
	return number - (number % (1 / 10 ** decimals))
