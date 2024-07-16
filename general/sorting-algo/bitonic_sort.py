# Bitonic Sort
# since lists are passed by reference, this function modifies the original list
# not working returns wrong results
def bitonic_sort(list, up=True):
	def bsort(arr, low, cnt, direction):
		if cnt > 1:
			k = cnt // 2
			bsort(arr, low, k, True)
			bsort(arr, low + k, k, False)
			bitonic_merge(arr, low, cnt, direction)

	def bitonic_merge(arr, low, cnt, direction):
		if cnt > 1:
			k = cnt // 2
			for i in range(low, low + k):
				if direction == (arr[i] > arr[i + k]):
					arr[i], arr[i + k] = arr[i + k], arr[i]
			bitonic_merge(arr, low, k, direction)
			bitonic_merge(arr, low + k, k, direction)
	bsort(list, 0, len(list), up)
	return list
