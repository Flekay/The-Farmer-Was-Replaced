# The next function takes an iterator and returns the next item in the iterator.
#
# Arguments:
#	- iterator (function): a function that returns the next item in the iterator
#
# Returns:
#	- any: the next item in the iterator
# Example:
#	- rx = iter(range(3))
#	- next(rx) # 0
#	- next(rx) # 1
def next(iterator):
	return iterator()
