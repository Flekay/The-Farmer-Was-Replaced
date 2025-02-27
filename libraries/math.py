e           = 2.718281828459045
pi          = 3.141592653589793
inf         = 10**309
ninf        = -inf
nan         = (-1)**0.5 # sqrt(-1) | inf-inf
tau         = 6.283185307179586
help        = "https://github.com/Flekay/The-Farmer-Was-Replaced/tree/main/general/math"
constants   = "[e, pi, inf, ninf, nan, tau]"
functions   = "[ceil, floor, isclose, ln, log, pow, root, round, sqrt, truncate]"

# Rounds a number up to the nearest integer.
#
# Arguments:
#	number (number): the number to round up
#
# Returns:
#	number: the rounded up number
#
# Example:
#	ceil(1.1)
#	# 2
def ceil(number):
	return -(-number // 1)

# Rounds a number down to the nearest integer.
#
# Arguments:
#	number (number): the number to round down
#
# Returns:
#	number: the rounded down number
#
# Example:
#	floor(1.9)
#	# 1
def floor(number):
	return number // 1

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

# The ln function calculates the natural logarithm of a number.
#
# Arguments:
#	x (number): the number to calculate the natural logarithm of
#
# Returns:
#	number: the natural logarithm of the number
#
# Example:
#	ln(2)
#	# 0.6931471805599453
def ln(x):
	return 10000 * ((x ** (0.0001)) - 1)

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

# Raises a number to a power.
#
# Arguments:
#	base (number): the base number
#	exponent (number): the exponent
#
# Returns:
#	number: the result of the base raised to the exponent
#
# Example:
#	pow(2, 3)
#	# 8
def pow(base, exponent):
	return base ** exponent

# The root function calculates the nth root of a number.
#
# Arguments:
#	number (number): the number to calculate the nth root of
#	n (number): the root to calculate
#
# Returns:
#	number: the nth root of the number
#
# Example:
#	root(8, 3)
#	# 2.0
def root(number, n):
	return number ** (1 / n)

# Rounds a number to a specified number of decimal places.
#
# Arguments:
#	number (number): the number to round
#	decimals (int): the number of decimal places to round to (default is 0)
#
# Returns:
#	number: the rounded number
#
# Example 1:
#	round(1.123456789)
#	# 1
def round(number, decimals=0):
	multiplier = 10 ** decimals
	if number >= 0:
		return (number * multiplier + 0.5) // 1 / multiplier
	else:
		return (number * multiplier - 0.5) // 1 / multiplier

# The sqrt function calculates the square root of a number.
#
# Arguments:
#	number (number): the number to calculate the square root of
#
# Returns:
#	number: the square root of the number
#
# Example:
#	sqrt(4)
#	# 2.0
def sqrt(number):
	return number ** 0.5

# Truncates a number to a specified number of decimal places.
#
# Arguments:
#	number (number): the number to truncate
#	decimals (int): the number of decimal places to truncate to (default is 0)
#
# Returns:
#	number: the truncated number
#
# Example 1:
#	truncate(1.123456789)
#	# 1
def truncate(number, decimals=0):
	return number - (number % (1 / 10 ** decimals))

