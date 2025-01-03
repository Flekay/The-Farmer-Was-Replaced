# Shell Sort
# since lists are passed by reference, this function modifies the original list
def shell_sort(list):
	n = len(list)
	gap = n // 2

	while gap > 0:
		for i in range(gap, n):
			temp = list[i]
			j = i
			while j >= gap and list[j - gap] > temp:
				list[j] = list[j - gap]
				j -= gap
			list[j] = temp
		gap //= 2
	return list
