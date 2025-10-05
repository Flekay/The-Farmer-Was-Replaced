# Replaces occurrences of a substring with a new substring.
#
# Arguments:
#	text (str): the input string
#	old (str): the substring to replace
#	new (str): the replacement substring
#
# Returns:
#	str: the modified string
#
# Example 1:
#	replace("hello world", "world", "there")
#	# 'hello there'
def replace(text, old, new):
	result = ""
	i = 0
	rep = 0
	len_old = len(old)
	if len_old > 1:
		while i < len(text):
			if text[i:i+len_old] == old:
				result += new
				rep += 1
				i += len_old
			else:
				result += text[i]
				i += 1
		return result
	else:
		for char in text:
			if char == old:
				result += new
				rep += 1
			else:
				result += char
		return result
