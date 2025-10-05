# Gets the value for a specified key with an optional default.
#
# Arguments:
#	dictionary (dict): the dictionary to search
#	key (str): the key to search for
#	default (any): the default value to return if the key is not found
#
# Returns:
#	any: the value for the key, or the default value if the key is not found
#
# Example 1:
#	dictionary = {'a': 1, 'b': 2}
#	get(dictionary, 'a')
#	# 1
#
# Example 2:
#	dictionary = {'a': 1, 'b': 2}
#	get(dictionary, 'c', 'default')
#	# 'default'
def get(dictionary, key, default=None):
	if dictionary and key in dictionary:
		return dictionary[key]
	return default
