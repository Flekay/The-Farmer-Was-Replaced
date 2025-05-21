# The iter function takes an iterable and returns a function that can be used to get the next item in the iterable.
#
# Arguments:
#	- iterable (iterable): an iterable object
#
# Returns:
#	- function: a function that can be passed to the next function to get the next item in the iterable
# Example:
#	- rx = iter(range(3))
#	- next(rx) # 0
#	- next(rx) # 1
def iter(iterable):
	items = list(iterable)
	items_len = len(items)
	index = [0]

	def next_item():
		i = index[0]
		if i < items_len:
			value = items[i]
			index[0] += 1
			return value
		return None

	return next_item
