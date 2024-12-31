
def do_swaps_high(i, j, measures, size):
	sm1 = size - 1

	if i<sm1 and j<sm1:
		m = measure()
		right = measure(East)
		up = measure(North)
		if m > right or m > up:
			if right < up:
				swap(East)
				measures[i][j] = right
				measures[i+1][j] = m
			else:
				swap(North)
				measures[i][j] = up
				measures[i][j+1] = m

	elif i<sm1:
		m = measure()
		right = measure(East)
		if m > right:
			swap(East)
			measures[i][j] = right
			measures[i+1][j] = m

	elif j<sm1:
		m = measure()
		up = measure(North)
		if m > up:
			swap(North)
			measures[i][j] = up
			measures[i][j+1] = m
			