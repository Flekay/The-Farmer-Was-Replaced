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
