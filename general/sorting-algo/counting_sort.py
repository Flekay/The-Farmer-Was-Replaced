# Counting Sort
# since lists are passed by reference, this function modifies the original list
def counting_sort(list):
	if len(list) == 0:
		return []
	max_val = max(list)
	min_val = min(list)
	range_of_elements = max_val - min_val + 1
	count = []
	for i in range(range_of_elements):
		count.append(0)
	output = []
	for i in range(len(list)):
		output.append(0)


	for i in range(len(list)):
		count[list[i] - min_val] += 1

	for i in range(1, len(count)):
		count[i] += count[i - 1]

	for i in range(len(list) - 1, -1, -1):
		output[count[list[i] - min_val] - 1] = list[i]
		count[list[i] - min_val] -= 1

	for i in range(len(list)):
		list[i] = output[i]
	return list
