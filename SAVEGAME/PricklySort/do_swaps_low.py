def do_swaps_low(i, j, measures, size):
	if i and j:
		m = measure()
		left = measure(West)
		down = measure(South)
		if m < left or m < down:
			if left > down:
				swap(West)
				measures[i][j] = left
				measures[i-1][j] = m
			else:
				swap(South)
				measures[i][j] = down
				measures[i][j-1] = m

	elif i:
		m = measure()
		left = measure(West)
		if m < left:
			swap(West)
			measures[i][j] = left
			measures[i-1][j] = m

	elif j:
		m = measure()
		down = measure(South)
		if m < down:
			swap(South)
			measures[i][j] = down
			measures[i][j-1] = m
			