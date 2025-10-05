# The copy function takes an object and returns a shallow copy of the object.
#
# Arguments:
#	object (object): an object
#
# Returns:
#	object: a shallow copy of the initial object
#
# Example:
#	copy([1, 2, 3])
#	# [1, 2, 3]
def copy(object):
	first_char = str(object)[0]
	if first_char == '[':
		return list(object)
	if first_char == '{':
		iter_set = set(object)
		if object == iter_set:
			return iter_set
		return dict(object)
	return object
