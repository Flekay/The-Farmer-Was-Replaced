# The enumerate function takes an iterable and returns an iterator that produces tuples of the index and the item.
#
# Arguments:
#	iterable (iterable): an iterable
#	start (int): the starting index (default is 0)
#
# Returns:
#	iterator: an iterator that produces tuples of the index and the item
#
# Example:
#	for index, item in enumerate([1, 2, 3]):
#		print(index, item)
def enumerate(iterable, start=0):
	results = []
	for item in iterable:
		results.append((start, item))
		start += 1
	return results
