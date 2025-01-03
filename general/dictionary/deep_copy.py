def deep_copy(dictionary, depth=0):
	if depth < 1:
		return dict(dictionary)
	new_dict = {}
	for key in dictionary:
		new_dict[key] = deep_copy(dictionary[key], depth - 1)
	return new_dict
