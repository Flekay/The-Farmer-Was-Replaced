# The Or function takes two boolean functions and returns the logical OR of them.
#
# Arguments:
#	f (bool functions): the first boolean functions
#	g (bool functions): the second boolean functions
#
# Returns:
#	bool functions: the logical OR of the two values
#
# Example:
#	Or(true, false)
#	# true
def Or(f, g):
	return f(true, g)
