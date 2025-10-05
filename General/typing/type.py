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
