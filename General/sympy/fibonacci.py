# Fibonacci numbers using Binet's formula
#
# Arguments:
#	n (int): the index of the Fibonacci number to compute
# Returns:
#	int: the nth Fibonacci number
# Example:
#	nth_fibonacci = fibonacci(10)
#	# print(nth_fibonacci)  # Output: 55
_sqrt5 = 5 ** 0.5
_phi = (1 + _sqrt5) / 2
_phi1 = 1 - _phi
def fibonacci(n):
	return (_phi ** n - _phi1 ** n) / _sqrt5
