# The average function takes a list of numbers and returns the average value.
#
# Arguments:
#	list (list): a list of numbers
#
# Returns:
#	number: the average value of the list
#
# Example:
#	list = [1, 2, 3]
#	average_value = average(list)
#	# 2
def average(list):
	total = 0
	for i in list:
		total += i
	return total / len(list)
