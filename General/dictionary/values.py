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
