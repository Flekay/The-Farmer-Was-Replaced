# The And function takes two boolean functions and returns the logical AND of them.
#
# Arguments:
#	f (bool functions): the first boolean functions
#	g (bool functions): the second boolean functions
#
# Returns:
#	bool functions: the logical AND of the two values
#
# Example:
#	And(true, false)
#	# false
def And(f, g):
	return f(g, false)
