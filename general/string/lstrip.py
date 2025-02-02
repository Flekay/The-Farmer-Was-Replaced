# Removes leading characters (default whitespace if chars is None) from the string.
#
# Arguments:
#	text (str): the input string
#	chars (str): the characters to remove (default is " " if None)
#
# Returns:
#	str: the trimmed string
#
# Example 1:
#	lstrip("   hello  ")
#	# 'hello  '
def lstrip(text, chars=" "):
	start = 0
	for char in text:
		if char not in chars:
			break
		start += 1
	return text[start:]
