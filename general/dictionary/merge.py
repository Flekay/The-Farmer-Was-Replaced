# Merges two dictionaries into one.
# ! If the dictionaries have the same key, the value from the right dictionary will be used.
#
# Arguments:
#	left (dict): the first dictionary to merge
#	right (dict): the second dictionary to merge
#
# Returns:
#	dict: the merged dictionary
#
# Example:
#	left = {'a': 1}
#	right = {'b': 2}
#	merged = merge(left, right)
#	# {'a': 1, 'b': 2}
def merge(left, right):
	for key in right:
		left[key] = right[key]
	return left
