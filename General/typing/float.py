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
# Float function takes a string or float and returns a float.
#
# Arguments:
#	x (string or float): the string or float to convert to an integer
#
# Returns:
#	number: the float value of the string or float
#
# Example:
#	x = "3.14"
#	int_value = int(x)
#	# 3.14
def float(x):
	number_str = str(x)
	if number_str == x:
		sign = 1
		idx = 0
		if number_str[0] == '-':
			sign = -1
			idx = 1
		integer_value = 0
		fraction_value = 0
		fraction_divisor = 1
		encountered_dot = False
		for ch in number_str[idx:]:
			if ch == '.':
				encountered_dot = True
				continue
			if not encountered_dot:
				integer_value = integer_value * 10 + _digits[ch]
			else:
				fraction_value = fraction_value * 10 + _digits[ch]
				fraction_divisor *= 10
		return sign * (integer_value + fraction_value / fraction_divisor)
	else:
		return x * 1.0
