# Comb sort
# since lists are passed by reference, this function modifies the original list
def comb_sort(list):
	def get_next_gap(gap):
		gap = (gap * 10) // 13
		if gap < 1:
			return 1
		return gap

	n = len(list)
	gap = n
	swapped = True

	while gap != 1 or swapped:
		gap = get_next_gap(gap)
		swapped = False

		for i in range(n - gap):
			if list[i] > list[i + gap]:
				list[i], list[i + gap] = list[i + gap], list[i]
				swapped = True
	return list
