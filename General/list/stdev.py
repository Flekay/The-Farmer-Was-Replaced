# The stdev function takes a list of numbers and returns the standard deviation.
#
# Arguments:
#	list (list): a list of numbers
#
# Returns:
#	number: the standard deviation of the list
# Example:
#	list = [1, 2, 3]
#	stdev_value = stdev(list)
#	# 0.816496580927726
def stdev(list):
	n = len(list)
	total = 0
	for x in list:
		total += x
	mean = total / n

	squared_diff_sum = 0.0
	for x in list:
		diff = x - mean
		squared_diff_sum += diff * diff

	variance = squared_diff_sum / (n - 1)
	return variance ** 0.5
