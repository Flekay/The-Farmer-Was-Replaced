# Converts a number to a string with an optional precision.
#
# Arguments:
#	number (number): the number to convert
#	precision (int): the number of decimal places to include (default is 4)
#
# Returns:
#	str: the number as a string
#
# Example 1:
#	string(1.234567)
#	# '1.2346'
def string(number, precision = 4):
	if number >= 0:
		string = str(number // 1)
	else:
		string = str(-(-number // 1))
	if precision > 0:
		string += "."
		number = abs(number)
		for _ in range(precision):
			number = (number * 10) % 10
			string += str(number // 1)
	return string
