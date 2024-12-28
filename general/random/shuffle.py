def shuffle(lst):
	for i in range(len(lst) - 1, 0, -1):
		j = random() * (i + 1)
		lst[i], lst[j] = lst[j], lst[i]
	return lst
