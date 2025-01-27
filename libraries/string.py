help        = "https://github.com/Flekay/The-Farmer-Was-Replaced/tree/main/general/string"
constants   = "[]"
functions   = "[join, string, strtime]"

# Joins a list of strings into a single string with an optional separator.
#
# Arguments:
#	list (list): the list of strings to join
#	separator (str): the separator to use between the strings (default is None)
#
# Returns:
#	str: the joined string
#
# Example 1:
#	join(['a', 'b', 'c'], ', ')
#	# 'a, b, c'
def join(list, separator=None):
	result = ""
	if separator:
		for string in list:
			result += string + separator
		return result[:-len(separator)]
	else:
		for string in list:
			result += string
		return result

# Converts a number to a string with an optional precision.
#
# Arguments:
#	number (number): the number to convert to a string
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
		string = str(number//1)
	else:
		string = str(-(-number // 1))
	if precision > 0:
		string += "."
		number = abs(number)
		for _ in range(precision):
			number = (number * 10) % 10
			string += str(number//1)
	return string

# Converts a number of seconds to a string in the format 'mm:ss.ff'.
#
# Arguments:
#	seconds (float): the number of seconds
#
# Returns:
#	str: the time string
#
# Example 1:
#	strtime(123.45)
#	# ' 2:03.45'
def strtime(seconds):
	# Flotating point error correction
	seconds += 0.00000000001

	# Format minutes
	if seconds >= 6000:
		min_str = str(seconds // 60)
	elif seconds >= 600:
		min_str = ' ' + str(seconds // 60)
	else:
		min_str = '  ' + str(seconds // 60)

	# Format seconds
	sec_str = "0123456789"[seconds // 10 % 6] + "0123456789"[seconds % 10]

	# Format fraction (2 digits)
	frac_str = "0123456789"[seconds * 10 % 10] + "0123456789"[seconds * 100 % 10]

	# Format fraction (4 digits)
	# frac_str = "0123456789"[seconds * 10 % 10] + "0123456789"[seconds * 100 % 10] + "0123456789"[seconds * 1000 % 10] + "0123456789"[seconds * 10000 % 10]

	# Construct the result string
	return min_str + ":" + sec_str + "." + frac_str

