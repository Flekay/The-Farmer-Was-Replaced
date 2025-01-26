# The sorted function sorts a list of numbers in-place in ascending order using the bucket sort algorithm.
#
# Arguments:
#	list (list): a list of numbers
#
# Returns:
#	list: a sorted list of numbers
#
# Example:
#	list = [3, 2, 1]
#	sorted_list = sorted(list)
#	# [1, 2, 3]
def sorted(list):
	if len(list) == 0:
		return []
	return_list = list + []
	min_value = min(list)
	max_value = max(list)

	# Number of buckets
	n = len(list)
	bucket_range = (max_value - min_value) // n + 1
	buckets = []
	for i in range(n):
		buckets.append([])

	# Put array elements in different buckets
	for num in return_list:
		index = (num - min_value) // bucket_range
		buckets[index].append(num)

	# Sort individual buckets using insertion sort
	for bucket in buckets:
		for i in range(1, len(bucket)):
			a = bucket[i]
			j = i - 1
			while j >= 0 and a < bucket[j]:
				bucket[j + 1] = bucket[j]
				j -= 1
			bucket[j + 1] = a

	# Concatenate all buckets into arr[]
	index = 0
	for bucket in buckets:
		for num in bucket:
			return_list[index] = num
			index += 1
	return return_list
