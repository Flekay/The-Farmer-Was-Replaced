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
