# IsClose function to compare floating point numbers with a tolerance
#
# Arguments:
#	a (number): the first number to compare
#	b (number): the second number to compare
#	rel_tol (number): the relative tolerance (optional, default is 1e-9)
#	abs_tol (number): the absolute tolerance (optional, default is 0.0)
#
# Returns:
#	bool: True if the numbers are close, False otherwise
#
# Example:
#	isclose(1, 1.000000001)
#	# True
def isclose(a, b, rel_tol=0.000000001, abs_tol=0.0):
	if a == b:
		return True
	diff = abs(a - b)
	if diff <= abs_tol:
		return True
	return diff <= rel_tol * max(a, b, -a, -b)
