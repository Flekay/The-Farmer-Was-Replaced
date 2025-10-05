# Tim Sort
# since lists are passed by reference, this function modifies the original list
def tim_sort(list):
	def insertion_sort(arr, left, right):
		for i in range(left + 1, right + 1):
			key = arr[i]
			j = i - 1
			while j >= left and arr[j] > key:
				arr[j + 1] = arr[j]
				j -= 1
			arr[j + 1] = key

	def merge(arr, l, m, r):
		len1, len2 = m - l + 1, r - m
		left, right = [], []

		for i in range(0, len1):
			left.append(arr[l + i])
		for i in range(0, len2):
			right.append(arr[m + 1 + i])

		i, j, k = 0, 0, l

		while i < len1 and j < len2:
			if left[i] <= right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1

		while i < len1:
			arr[k] = left[i]
			k += 1
			i += 1

		while j < len2:
			arr[k] = right[j]
			k += 1
			j += 1

	min_run = 32
	n = len(list)

	for i in range(0, n, min_run):
		insertion_sort(list, i, min((i + min_run - 1), n - 1))

	size = min_run
	while size < n:
		for start in range(0, n, size * 2):
			mid = start + size - 1
			end = min((start + size * 2 - 1), n - 1)

			if mid < end:
				merge(list, start, mid, end)

		size *= 2
	return list
