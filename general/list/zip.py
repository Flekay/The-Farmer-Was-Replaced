# The zip function takes a list of lists and returns a list of tuples where the i-th tuple contains the i-th element from each of the argument lists.
#
# Arguments:
#	arrays (list): a list of lists
#
# Returns:
#	list: a list of tuples where the i-th tuple contains the i-th element from each of the argument lists
#
# Example:
#	lists_to_zip = [
#		[1,2,3],
#		['a','b','c'],
#		[True,False,True]
#	]
#	zipped = zip(lists_to_zip)
#	# [(1,'a',True), (2,'b',False), (3,'c',True)]
def zip(arrays):
	results = []
	min_length = len(arrays[0])
	for arr in arrays:
		if len(arr) < min_length:
			min_length = len(arr)
	min_length = range(min_length)

	for i in min_length:
		current_tuple = []
		for arr in arrays:
			current_tuple.append(arr[i])
		results.append(current_tuple)

	return results
