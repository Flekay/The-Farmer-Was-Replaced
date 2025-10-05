# The log function calculates the logarithm of a number.
#
# Arguments:
#	number (number): the number to calculate the logarithm of
#	base (number): the base of the logarithm (default is e)
#
# Returns:
#	number: the logarithm of the number
#
# Example:
#	log(2)
#	# 0.6931471805599453
def log(number, base=2.718281828459045):
	exp = 0.00000001
	return (number**(exp) - 1) / (base**(exp) - 1)
