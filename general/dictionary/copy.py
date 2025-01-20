# Creates a shallow copy of a dictionary.
#
# Arguments:
#	dictionary (dict): the dictionary to copy
#
# Returns:
#	dict: a shallow copy of the dictionary
#
# Example:
#	old_dict = {'a': 1, 'b': 2}
#	new_dict = copy(old_dict)
def copy(dictionary):
	return dict(dictionary)
