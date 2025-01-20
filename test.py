def is_sorted(arr):
	for i in range(len(arr) - 1):
		if arr[i] > arr[i+1]:
			return False
	return True

def is_sorted2(arr):
	for i in range(1, len(arr)):
		if arr[i-1] > arr[i]:
			return False
	return True

def is_sorted3(arr):
	if not arr:
		return True
	arm1 = arr[0]
	for i in arr:
		if i < arm1:
			return False
		arm1 = i
	return True

def is_sorted(list):
	for i in list:
		arm1 = i
		break
	for i in list:
		if i < arm1:
			return False
		arm1 = i
	return True

list = [] # empty list
# list = [1] # single element list
# list = [1,1] # duplicate element list
# list = [1,2,3,4,5,6,7,8,9] # sorted list
# list = [9,8,7,6,5,4,3,2,1] # reverse sorted list
# list = [1,2,3,4,8,5,6,7,8] # unsorted list
# list = [-3, -2, -1, 0, 1, 2, 3, 4, 5] # sorted list with negative numbers

ticks = get_tick_count()
quick_print(is_sorted(list))
quick_print("is_sorted", get_tick_count() - ticks)

ticks = get_tick_count()
quick_print(is_sorted2(list))
quick_print("is_sorted2", get_tick_count() - ticks)

ticks = get_tick_count()
quick_print(is_sorted3(list))
quick_print("is_sorted3", get_tick_count() - ticks)

ticks = get_tick_count()
quick_print(is_sorted4(list))
quick_print("is_sorted4", get_tick_count() - ticks)

if is_sorted(list) != is_sorted2(list) or is_sorted(list) != is_sorted3(list):
	quick_print("Error")
