# Filters a dictionary based on a predicate function.
#
# Arguments:
#	dictionary (dict): the dictionary to filter
#	predicate (function): the predicate function
#
# Returns:
#	dict: the filtered dictionary
#
# Example:
#	def is_even(value):
#		return value % 2 == 0
#
#	dictionary = {'a': 1, 'b': 2, 'c': 3}
#	filtered = filter(dictionary, is_even)
#	# {'b': 2}
def filter(dictionary, predicate):
	filtered = {}
	for key in dictionary:
		if predicate(dictionary[key]):
			filtered[key] = dictionary[key]
	return filtered
