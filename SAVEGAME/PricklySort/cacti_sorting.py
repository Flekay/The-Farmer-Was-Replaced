def cacti_sorting(grid):
	size=get_world_size()
	sm1 = size - 1
	rn = range(size)
	rrn = range(sm1, -1, -1)

	for s in range(9):
		for x in rn:
			grid_x = grid[x]
			for y in rn:
				cur = grid_x[y]
				if cur == s:
					low_insertion(x, y, cur, grid, size, sm1)

		s = 9 - s
		for x in rrn:
			grid_x = grid[x]
			for y in rrn:
				cur = grid_x[y]
				if cur == s:
					high_insertion(x, y, cur, grid, size, sm1)

	harvest()
	