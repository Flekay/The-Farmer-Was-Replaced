# Selection Sort
# since lists are passed by reference, this function modifies the original list
def selection_sort(list):
	sorted_numbers = list
	n = len(sorted_numbers)
	for s in range(n):
		min_idx = s
		for i in range(s + 1, n):
			if sorted_numbers[i] < sorted_numbers[min_idx]:
				min_idx = i
		(sorted_numbers[s], sorted_numbers[min_idx]) = (sorted_numbers[min_idx], sorted_numbers[s])
	return list

# since resuls are returned, the original list is not modified
def compact_selection_sort(list):
	res = []
	while list:
		m = min(list)
		res.append(m)
		list.remove(m)
	return res
