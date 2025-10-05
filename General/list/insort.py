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
