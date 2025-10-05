# Returns a deep copy of an iterable.
#
# Arguments:
#	object (iterable): an iterable
#
# Returns:
#	iterable: a deep copy of the iterable
#
# Example:
#	x = {1: [1, 2, 3], (1, 2): {1, 2, 3}}
#	y = deepcopy(x)
#	{1: [1, 2, 3], (1, 2): {1, 2, 3}}
def deepcopy(object):
	first_char = str(object)[0]
	if first_char == '[':
		new_list = []
		for item in object:
			new_list.append(deepcopy(item))
		return new_list
	if first_char == '{':
		if object == set(object):
			new_set = set()
			for item in object:
				new_set.add(deepcopy(item))
			return new_set
		new_dict = {}
		for key in object:
			new_dict[key] = deepcopy(object[key])
		return new_dict
	return object
