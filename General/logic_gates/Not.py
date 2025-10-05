# The Not function takes a boolean function and returns the logical NOT of it.
#
# Arguments:
#	f (bool functions): the boolean function
#
# Returns:
#	bool functions: the logical NOT of the value
#
# Example:
#	Not(true)
#	# false
def Not(f):
	return f(false, true)
