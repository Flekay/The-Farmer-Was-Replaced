def do_swaps_lower(x, y, measures, size, sm1):
	if x and y:
		cur = measure()
		left = measure(West)
		down = measure(South)
		if cur < left or cur < down:
			if left > down:
				swap(West)
				measures[x][y] = left
				measures[x-1][y] = cur
			else:
				swap(South)
				measures[x][y] = down
				measures[x][y-1] = cur

	elif x:
		cur = measure()
		left = measure(West)
		if cur < left:
			swap(West)
			measures[x][y] = left
			measures[x-1][y] = cur

	elif y:
		cur = measure()
		down = measure(South)
		if cur < down:
			swap(South)
			measures[x][y] = down
			measures[x][y-1] = cur
			