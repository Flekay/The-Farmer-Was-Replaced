def merge(left, right):
	for key in right:
		left[key] = right[key]
	return left
