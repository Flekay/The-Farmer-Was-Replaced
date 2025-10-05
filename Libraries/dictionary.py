help        = "https://github.com/Flekay/The-Farmer-Was-Replaced/tree/main/general/dictionary"
constants   = "[]"
functions   = "[filter, get, items, keys, merge, set, values]"

# Filters a dictionary based on a predicate function.
#
# Arguments:
#	dictionary (dict): the dictionary to filter
#	predicate (function): the predicate function
#
# Returns:
#	dict: the filtered dictionary
#
# Example:
#	def is_even(value):
#		return value % 2 == 0
#
#	dictionary = {'a': 1, 'b': 2, 'c': 3}
#	filtered = filter(dictionary, is_even)
#	# {'b': 2}
def filter(dictionary, predicate):
	filtered = {}
	for key in dictionary:
		if predicate(dictionary[key]):
			filtered[key] = dictionary[key]
	return filtered

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

# Retrieves all the keys from a dictionary and returns them as a list.
#
# Arguments:
#	dictionary (dict): the dictionary to retrieve keys from
#
# Returns:
#	list: a list of keys from the dictionary
#
# Example:
#	dictionary = {'a': 1, 'b': 2}
#	keys = keys(dictionary)
#	# ['a', 'b']
def keys(dictionary):
	return list(dictionary)

# Merges two dictionaries into one.
# ! If the dictionaries have the same key, the value from the right dictionary will be used.
#
# Arguments:
#	left (dict): the first dictionary to merge
#	right (dict): the second dictionary to merge
#
# Returns:
#	dict: the merged dictionary
#
# Example:
#	left = {'a': 1}
#	right = {'b': 2}
#	merged = merge(left, right)
#	# {'a': 1, 'b': 2}
def merge(left, right):
	for key in right:
		left[key] = right[key]
	return left

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

# Retrieves all the values from a dictionary and returns them as a list.
#
# Arguments:
#	dictionary (dict): the dictionary to retrieve values from
#
# Returns:
#	list: a list of values from the dictionary
#
# Example:
#	dictionary = {'a': 1, 'b': 2}
#	values = values(dictionary)
#	# [1, 2]
def values(dictionary):
	values = []
	for key in dictionary:
		values.append(dictionary[key])
	return values

