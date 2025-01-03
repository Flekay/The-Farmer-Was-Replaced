# Concatenate the strings in the list
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
