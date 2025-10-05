# Finds the first occurrence of a substring in the string.
#
# Arguments:
#	text (str): the input string
#	value (str): the substring to find
#
# Returns:
#	int: the index of the first occurrence of the substring (or -1 if not found)
#
# Example 1:
#	find("hello world", "world")
#	# 6
def find(text, value):
	value_len = len(value)
	if value_len > 1:
		i = 0
		while i < len(text):
			if text[i:i+value_len] == value:
				return i
			i += 1
	else:
		i = 0
		for char in text:
			if char == value:
				return i
			i += 1
	return -1
