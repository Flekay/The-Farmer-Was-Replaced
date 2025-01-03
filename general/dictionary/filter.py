def filter(dictionary, predicate):
	filtered = {}
	for key in dictionary:
		if predicate(dictionary[key]):
			filtered[key] = dictionary[key]
	return filtered
