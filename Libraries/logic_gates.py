help        = "https://github.com/Flekay/The-Farmer-Was-Replaced/tree/main/general/logic_gates"
constants   = "[]"
functions   = "[And, false, Not, Or, true]"

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

# The false function returns the second value.
#
# Arguments:
#	a (bool functions): the first value
#	b (bool functions): the second value
#
# Returns:
#	bool functions: the second value
#
# Example:
#	false(true, false)
#	# false
def false(a, b):
	return b

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

# The true function returns the first value.
#
# Arguments:
#	a (bool functions): the first value
#	b (bool functions): the second value
#
# Returns:
#	bool functions: the first value
#
# Example:
#	true(true, false)
#	# true
def true(a, b):
	return a

