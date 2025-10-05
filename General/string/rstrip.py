# Removes trailing characters from the string.
#
# Arguments:
#	text (str): the input string
#	chars (str): the characters to remove
#
# Returns:
#	str: the trimmed string
#
# Example 1:
#	rstrip("  hello   ")
#	# '  hello'
def rstrip(text, chars=" "):
	end = len(text)-1
	for end in range(end, -1, -1):
		if text[end] not in chars:
			break
	return text[:end+1]
