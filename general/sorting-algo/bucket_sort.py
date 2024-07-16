# Bucket Sort
# requires the insertion_sort function
# since lists are passed by reference, this function modifies the original list
def bucket_sort(list):
	if len(list) == 0:
		return []
	min_value = min(list)
	max_value = max(list)

	# Number of buckets
	n = len(list)
	bucket_range = (max_value - min_value) // n + 1
	buckets = []
	for i in range(n):
		buckets.append([])

	# Put array elements in different buckets
	for num in list:
		index = (num - min_value) // bucket_range
		buckets[index].append(num)

	# Sort individual buckets using insertion sort
	for bucket in buckets:
		insertion_sort(bucket)

	# Concatenate all buckets into arr[]
	index = 0
	for bucket in buckets:
		for num in bucket:
			list[index] = num
			index += 1
	return list

# since resuls are returned, the original list is not modified
def compact_bucket_sort(arr):
	if not arr:
		return arr

	# Find min and max values
	min_value = min(arr)
	max_value = max(arr)

	# Create buckets
	num_buckets = len(arr)
	bucket_range = (max_value - min_value) // num_buckets + 1
	buckets = []
	for i in range(num_buckets):
		buckets.append([])

	# Distribute elements into buckets
	for num in arr:
		index = (num - min_value) // bucket_range
		buckets[index].append(num)

	# Sort buckets using our compact insertion sort
	def compact_insertion_sort(bucket):
		sorted_portion = []
		for item in bucket:
			if not sorted_portion:
				sorted_portion.append(item)
			else:
				low = 0
				high = len(sorted_portion)
				while low < high:
					mid = (low + high) // 2
					if sorted_portion[mid] < item:
						low = mid + 1
					else:
						high = mid
				sorted_portion.insert(low, item)
		return sorted_portion

	# Sort each bucket and combine results
	sorted_arr = []
	for bucket in buckets:
		sorted_arr = sorted_arr + compact_insertion_sort(bucket)

	return sorted_arr
