# The sorted function takes a list of numbers and returns a new list with the numbers sorted in ascending order.
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
def sorted(input_list):
	if not input_list:
		return []

	min_value = min(input_list)
	max_value = max(input_list)

	n = len(input_list)
	bucket_range = (max_value - min_value) // n + 1

	# Create empty buckets
	buckets = []
	for _ in range(n):
		buckets.append([])

	# Distribute elements into buckets
	for num in input_list:
		index = (num - min_value) // bucket_range
		buckets[index].append(num)

	# Sort each bucket using insertion sort
	for bucket in buckets:
		if bucket:
			for i in range(1, len(bucket)):
				key = bucket[i]
				j = i - 1
				while j >= 0 and key < bucket[j]:
					bucket[j + 1] = bucket[j]
					j -= 1
				bucket[j + 1] = key

	# Merge buckets
	output = []
	for bucket in buckets:
		for num in bucket:
			output.append(num)

	return output
