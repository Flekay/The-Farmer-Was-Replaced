# Returns a list of unique elements from a given list.
#
# Arguments:
#	lst (list): the list to retrieve unique elements from
#
# Returns:
#	list: a list of unique elements from the given list
#
# Example:
#	lst = [1, 2, 3, 2, 1]
#	unique_lst = unique(lst)
#	# [1, 2, 3]
def unique(lst):
	return list(set(lst))
