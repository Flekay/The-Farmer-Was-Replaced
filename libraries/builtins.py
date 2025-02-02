help        = "https://github.com/Flekay/The-Farmer-Was-Replaced/tree/main/general/builtins"
constants   = "[]"
functions   = "[copy, deepcopy, help, uniqid, enumerate, raise]"

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

# Prints a help message for a module.
#
# Arguments:
#	module (module): the module to print help for
#
# Example:
#	import math
#	help(math)
def help(module):
	quick_print(module.__name__, "Help")
	quick_print("functions:")
	quick_print(module.functions)
	quick_print("")
	quick_print("constants:")
	quick_print(module.constants)
	return ""

# Raises an exception with an optional argument.
#
# Arguments:
#	x (Any): the argument related to the exception; it can be of any type.
#
# Example:
#	raise("This is an error message.")
#	# This is an error message.
def raise(x=None):
	if msg:
		quick_print(x)
	[] = [[],[]]

_id_counter = 0
# Generates a unique identifier.
#
# Returns:
#	int: a unique identifier
#
# Example:
#	uniqid()
#	# 1
def uniqid():
	global _id_counter
	_id_counter += 1
	return _id_counter

