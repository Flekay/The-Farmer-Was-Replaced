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
