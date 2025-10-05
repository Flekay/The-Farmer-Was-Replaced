# Shuffles a list in place.
#
# Arguments:
#	lst (list): the list to shuffle
#
# Returns:
#	list: the shuffled list
#
# Example:
#	shuffle([1, 2, 3])
#	# [2, 1, 3]
def shuffle(lst):
	for i in range(len(lst) - 1, 0, -1):
		j = random() * (i + 1)
		temp = lst[i]
		lst[i] = lst[j]
		lst[j] = temp
	return lst
