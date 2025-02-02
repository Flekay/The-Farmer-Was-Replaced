# Splits the string into a list of words.
#
# Arguments:
#	text (str): the input string
#	sep (str): the separator to split the string by (default is " ")
#
# Returns:
#	list: the list of words
#
# Example 1:
#	split("hello world")
#	# ['hello', 'world']
def split(text, sep=" "):
	sep_len = len(sep)
	result = []
	if sep_len > 1:
		word = ""
		i = 0
		while i < len(text):
			if text[i:i+sep_len] == sep:
				result.append(word)
				word = ""
				i += sep_len
			else:
				word += text[i]
				i += 1
		result.append(word)
		return result
	else:
		word = ""
		for char in text:
			if char == sep:
				result.append(word)
				word = ""
			else:
				word += char
		result.append(word)
		return result
