help        = "https://github.com/Flekay/The-Farmer-Was-Replaced/tree/main/general/list"
constants   = "[]"
functions   = "[average, insort, is_sorted, mean, median, reversed, sorted, sum, unique, zip]"

# The average function takes a list of numbers and returns the average value.
#
# Arguments:
#	list (list): a list of numbers
#
# Returns:
#	number: the average value of the list
#
# Example:
#	list = [1, 2, 3]
#	average_value = average(list)
#	# 2
def average(list):
	total = 0
	for i in list:
		total += i
	return total / len(list)

# The insort function takes a list and an item, and inserts the item into the list in sorted order.
#
# Arguments:
#	list (list): a list of numbers
#	item (number): the number to insert into the list
#
# Returns:
#	None
#
# Example:
#	list = [1, 3, 4]
#	insort(list, 2)
#	[1, 2, 3, 4]
def insort(list, item):
	lo = 0
	hi = len(list)
	while lo < hi:
		mid = (lo + hi) // 2
		if list[mid] < item:
			lo = mid + 1
		else:
			hi = mid
	list.insert(lo, item)

# The is_sorted function takes a list of numbers and returns True if the list is sorted in ascending order, otherwise False.
#
# Arguments:
#	list (list): a list of numbers
#
# Returns:
#	boolean: True if the list is sorted in ascending order, otherwise False
#
# Example:
#	list = [1, 2, 3]
#	is_sorted_list = is_sorted(list)
#	# True
def is_sorted(list):
	for i in list:
		arm1 = i
		break
	for i in list:
		if i < arm1:
			return False
		arm1 = i
	return True

# The mean function takes a list of numbers and returns the mean value.
#
# Arguments:
#	list (list): a list of numbers
#
# Returns:
#	number: the mean value of the list
#
# Example:
#	list = [1, 2, 3]
#	mean_value = mean(list)
#	# 2
def mean(list):
	total = 0
	for i in list:
		total += i
	return total / len(list)

# The median function takes a list of numbers and returns the median value.
#
# Arguments:
#	list (list): a list of numbers
#
# Returns:
#	number: the median value of the list
#
# Example:
#	list = [1, 2, 3]
#	median_value = median(list)
#	# 2
def median(list):
	sorted_numbers = sorted(list)
	length = len(sorted_numbers)

	if length % 2 == 1:
		return sorted_numbers[length // 2]
	else:
		middle_right = length // 2
		middle_left = middle_right - 1
		return (sorted_numbers[middle_left] + sorted_numbers[middle_right]) / 2

# The reversed function takes a list and returns a new list with the elements in reverse order.
#
# Arguments:
#	list (list): a list of elements
#
# Returns:
#	list: a new list with the elements in reverse order
#
# Example:
#	list = [1, 2, 3]
#	reversed_list = reversed(list)
#	# [3, 2, 1]
def reversed(list):
	return list[::-1]

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

# Returns the sum of all elements in a list.
#
# Arguments:
#	list (list): the list to sum
#
# Returns:
#	number: the sum of all elements in the list
#
# Example:
#	list = [1, 2, 3]
#	total = sum(list)
#	# 6
def sum(list):
	total = 0
	for i in list:
		total += i
	return total

# Returns a list of unique elements from a given list.
#
# Arguments:
#	lst (list): the list to retrieve unique elements from
#
# Returns:
#	list: a list of unique elements from the given list
#
# Example:
#	lst = [1, 2, 3, 2, 1]
#	unique_lst = unique(lst)
#	# [1, 2, 3]
def unique(lst):
	return list(set(lst))

# The zip function takes a list of lists and returns a list of tuples where the i-th tuple contains the i-th element from each of the argument lists.
#
# Arguments:
#	arrays (list): a list of lists
#
# Returns:
#	list: a list of tuples where the i-th tuple contains the i-th element from each of the argument lists
#
# Example:
#	lists_to_zip = [
#		[1,2,3],
#		['a','b','c'],
#		[True,False,True]
#	]
#	zipped = zip(lists_to_zip)
#	# [(1,'a',True), (2,'b',False), (3,'c',True)]
def zip(arrays):
	results = []
	min_length = len(arrays[0])
	for arr in arrays:
		if len(arr) < min_length:
			min_length = len(arr)
	min_length = range(min_length)

	for i in min_length:
		current_tuple = []
		for arr in arrays:
			current_tuple.append(arr[i])
		results.append(current_tuple)

	return results

