# Returns the sum of all elements in a list.
#
# Arguments:
#	list (list): the list to sum
#
# Returns:
#	number: the sum of all elements in the list
#
# Example:
#	list = [1, 2, 3]
#	total = sum(list)
#	# 6
def sum(list):
	total = 0
	for i in list:
		total += i
	return total
