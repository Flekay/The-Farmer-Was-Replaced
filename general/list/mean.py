# The mean function takes a list of numbers and returns the mean value.
#
# Arguments:
#	list (list): a list of numbers
#
# Returns:
#	number: the mean value of the list
#
# Example:
#	list = [1, 2, 3]
#	mean_value = mean(list)
#	# 2
def mean(list):
	total = 0
	for i in list:
		total += i
	return total / len(list)
