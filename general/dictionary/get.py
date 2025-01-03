def get(dictionary, key, default=None):
	if dictionary and key in dictionary:
		return dictionary[key]
	return default
