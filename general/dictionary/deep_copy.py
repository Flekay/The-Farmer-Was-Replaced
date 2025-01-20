# Creates a deep copy of a dictionary up to a specified depth.
#
# Arguments:
#	dictionary (dict): the dictionary to copy
#	depth (int): the number of levels deep to copy
#
# Returns:
#	dict: a deep copy of the dictionary
#
# Example:
#	old_dict = {'a': {'b': 1}}
#	new_dict = deep_copy(old_dict, 1)
def deep_copy(dictionary, depth=0):
	if depth < 1:
		return dict(dictionary)
	new_dict = {}
	for key in dictionary:
		new_dict[key] = deep_copy(dictionary[key], depth - 1)
	return new_dict
