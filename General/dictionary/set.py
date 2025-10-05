# Sets a key-value pair in a dictionary.
#
# Arguments:
#	dictionary (dict): the dictionary to modify
#	key (any): the key to set
#	value (any): the value to set
#
# Returns:
#	dict: the modified dictionary
#
# Example:
#	dictionary = {'a': 1}
#	set(dictionary, 'b', 2)
#	# {'a': 1, 'b': 2}
def set(dictionary, key, value):
	dictionary[key] = value
	return dictionary
