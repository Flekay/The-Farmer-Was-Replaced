def deep_copy_list(xs, depth=0):
	if depth < 1:
		return list(xs)
	new_dict = []
	i = 0
	for _ in xs:
		new_dict.append(deep_copy_list(xs[i], depth - 1))
		i += 1
	return new_dict
