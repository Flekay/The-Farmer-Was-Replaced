_digits = {
	'0': 0,
	'1': 1,
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'-': 0,
}
# Integer function takes a string or float and returns an integer.
#
# Arguments:
#	x (string or float): the string or float to convert to an integer
#
# Returns:
#	number: the integer value of the string or float
#
# Example:
#	x = 3.14
#	int_value = int(x)
#	# 3
def int(x):
	number_str = str(x)
	if number_str == x:
		number = 0
		for ch in number_str:
			if ch == '.':
				break
			number = number * 10 + _digits[ch]
		if number_str[0] == '-':
			number = -number
		return number
	elif x > 0:
		return x // 1
	else:
		return -(-x // 1)
