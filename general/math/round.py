# Rounds a number to a specified number of decimal places.
#
# Arguments:
#	number (number): the number to round
#	decimals (int): the number of decimal places to round to (default is 0)
#
# Returns:
#	number: the rounded number
#
# Example 1:
#	round(1.123456789)
#	# 1
def round(number, decimals=0):
	multiplier = 10 ** decimals
	if number >= 0:
		return (number * multiplier + 0.5) // 1 / multiplier
	else:
		return (number * multiplier - 0.5) // 1 / multiplier
