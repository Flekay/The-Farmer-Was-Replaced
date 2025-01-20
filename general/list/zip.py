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

# Example usage:
# lists_to_zip = [
# 	[1,2,3],
# 	['a','b','c'],
# 	[True,False,True]
# ]
# zipped = zip(lists_to_zip)  # [(1,'a',True), (2,'b',False), (3,'c',True)]

# quick_print(zipped)
