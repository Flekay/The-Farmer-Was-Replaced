# The is_sorted function takes a list of numbers and returns True if the list is sorted in ascending order, otherwise False.
#
# Arguments:
#	list (list): a list of numbers
#
# Returns:
#	boolean: True if the list is sorted in ascending order, otherwise False
#
# Example:
#	list = [1, 2, 3]
#	is_sorted_list = is_sorted(list)
#	# True
def is_sorted(list):
	for i in list:
		arm1 = i
		break
	for i in list:
		if i < arm1:
			return False
		arm1 = i
	return True
