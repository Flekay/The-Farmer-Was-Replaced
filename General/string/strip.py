# Removes both leading and trailing characters (default whitespace if chars is None) from the string.
#
# Arguments:
#	text (str): the input string
#	chars (str): the characters to remove (default is " " if None)
#
# Returns:
#	str: the trimmed string
#
# Example 1:
#	strip("   hello   ")
#	# 'hello'
def strip(text, chars=" "):
	start = 0
	for char in text:
		if char not in chars:
			break
		start += 1
	end = len(text)-1
	for end in range(end, start-1, -1):
		if text[end] not in chars:
			break
	return text[start:end+1]
