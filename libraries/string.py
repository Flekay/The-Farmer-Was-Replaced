help        = "https://github.com/Flekay/The-Farmer-Was-Replaced/tree/main/general/string"
constants   = "[]"
functions   = "[join, string, strtime, rstrip, lstrip, strip, zfill, replace, split, find]"

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

# Pads the string on the left with zeros until its length equals the given width.
#
# Arguments:
#	text (str): the input string
#	width (int): the desired total length
#
# Returns:
#	str: the padded string
#
# Example 1:
#	zfill("42", 5)
#	# '00042'
def zfill(text, width):
	result = ""
	for _ in range(width - len(text)):
		result += "0"
	return result + text

