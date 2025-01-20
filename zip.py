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




# counterclockwise

def zip(arrays):
	results = []
	min_length = len(arrays[0])
	i = 0
	for arr in arrays:
		arrays[i] = arr[::-1]
		i +=1
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
matrix = []
for x in range(get_world_size()):
  line = []
  for y in range(get_world_size()):
    line.append((x,y))
  matrix.append(line)
zipped = zip(matrix[::-1])  # [(1,'a',True), (2,'b',False), (3,'c',True)]
#zipped = zip(zipped[::-1])  # [(1,'a',True), (2,'b',False), (3,'c',True)]
#zipped = zip(zipped[::-1])  # [(1,'a',True), (2,'b',False), (3,'c',True)]

i = 0
for arr in matrix:
	matrix[i] = arr[::-1]
	i +=1
for list in matrix:
	quick_print(list)

