def do_swaps_higher(x, y, measures, size, sm1):
	if x<sm1 and y<sm1:
		cur = measure()
		right = measure(East)
		up = measure(North)
		if cur > right or cur > up:
			if right < up:
				swap(East)
				measures[x][y] = right
				measures[x+1][y] = cur
			else:
				swap(North)
				measures[x][y] = up
				measures[x][y+1] = cur

	elif x<sm1:
		cur = measure()
		right = measure(East)
		if cur > right:
			swap(East)
			measures[x][y] = right
			measures[x+1][y] = cur

	elif y<sm1:
		cur = measure()
		up = measure(North)
		if cur > up:
			swap(North)
			measures[x][y] = up
			measures[x][y+1] = cur
			