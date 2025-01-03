# Radix Sort
# since lists are passed by reference, this function modifies the original list
def radix_sort(list):
	if len(list) == 0:
		return []
	def counting_sort_for_radix(arr, exp):
		n = len(arr)
		output = []
		for i in range(n):
			output.append(0)
		count = []
		for i in range(10):
			count.append(0)


		for i in range(n):
			index = arr[i] // exp
			count[index % 10] += 1

		for i in range(1, 10):
			count[i] += count[i - 1]

		for i in range(n - 1, -1, -1):
			index = arr[i] // exp
			output[count[index % 10] - 1] = arr[i]
			count[index % 10] -= 1

		for i in range(n):
			arr[i] = output[i]
	max_val = max(list)
	exp = 1
	while max_val // exp > 0:
		counting_sort_for_radix(list, exp)
		exp *= 10
	return list
