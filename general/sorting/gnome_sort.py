# Gnome Sort
# since lists are passed by reference, this function modifies the original list
def gnome_sort(list):
	n = len(list)
	index = 0
	while index < n:
		if index == 0 or list[index] >= list[index - 1]:
			index += 1
		else:
			list[index], list[index - 1] = list[index - 1], list[index]
			index -= 1
	return list
