# Retrieves all key-value pairs from a dictionary.
#
# Arguments:
#	dictionary (dict): the dictionary to retrieve items from
#
# Returns:
#	list: a list of key-value pairs from the dictionary
#
# Example:
#	dictionary = {'a': 1, 'b': 2}
#	items = dictionary_items(dictionary)
#	# [('a', 1), ('b', 2)]
def dictionary_items(dictionary):
	items = []
	for key in dictionary:
		items.append((key, dictionary[key]))
	return items
