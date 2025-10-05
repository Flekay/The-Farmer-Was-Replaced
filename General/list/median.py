# The median function takes a list of numbers and returns the median value.
#
# Arguments:
#	list (list): a list of numbers
#
# Returns:
#	number: the median value of the list
#
# Example:
#	list = [1, 2, 3]
#	median_value = median(list)
#	# 2
def median(list):
	sorted_numbers = sorted(list)
	length = len(sorted_numbers)

	if length % 2 == 1:
		return sorted_numbers[length // 2]
	else:
		middle_right = length // 2
		middle_left = middle_right - 1
		return (sorted_numbers[middle_left] + sorted_numbers[middle_right]) / 2
