help        = "https://github.com/Flekay/The-Farmer-Was-Replaced/tree/main/general/typing"
constants   = "[]"
functions   = "[float, int, isinstance, type]"

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

# The isinstance function checks if a variable is of a certain type.
#
# Arguments:
#	object (variable): a variable
#	expected_type (string): the expected type of the variable
#
# Returns:
#	bool: True if the variable is of the expected type, False otherwise
#
# Example:
#	x = 1
#	x_is_number = isinstance(x, 'number')
#	# True
def isinstance(object, expected_type):
	if object == None:
		return 'none' == expected_type
	object_str = str(object)
	if object == object_str:
		return 'string' == expected_type
	object_str = object_str[0]
	if object_str == '[':
		return 'list' == expected_type
	if object_str in "-0123456789":
		return 'number' == expected_type
	if object_str in "TF":
		return 'bool' == expected_type
	if object_str == '{':
		if object == set(object):
			return 'set' == expected_type
		return 'dict' == expected_type
	if object_str == '(':
		return 'tuple' == expected_type
	if object_str == '<':
		return 'module' == expected_type
	return 'function' == expected_type

# The type function takes a variable and returns the type of the variable as a string.
#
# Arguments:
#	x (variable): a variable
#
# Returns:
#	string: the type of the variable
#
# Example:
#	x = 1
#	x_type = type(x)
#	# 'number'
def type(x):
	if x == None:
		return 'none'
	x_str = str(x)
	if x == x_str:
		return 'string'
	x_str = x_str[0]
	if x_str == '[':
		return 'list'
	if x_str in "-0123456789":
		return 'number'
	if x_str in "TF":
		return 'bool'
	if x_str == '{':
		if x == set(x):
			return 'set'
		return 'dict'
	if x_str == '(':
		return 'tuple'
	if x_str == '<':
		return 'module'
	return 'function'

