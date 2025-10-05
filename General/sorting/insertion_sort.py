# Insertion Sort
# since lists are passed by reference, this function modifies the original list
def insertion_sort(list):
	for i in range(1, len(list)):
		a = list[i]
		j = i - 1
		while j >= 0 and a < list[j]:
			list[j + 1] = list[j]
			j -= 1
		list[j + 1] = a
	return list

# since resuls are returned, the original list is not modified
def compact_insertion_sort(list):
	sorted_portion = []
	for item in list:
		# custom insort() function
		if not sorted_portion:
			sorted_portion.append(item)
		else:
			low, high = 0, len(sorted_portion)
			while low < high:
				mid = (low + high) // 2
				if sorted_portion[mid] < item:
					low = mid + 1
				else:
					high = mid
			sorted_portion.insert(low, item)
	return sorted_portion
