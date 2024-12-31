
def init2():
	ws = get_world_size()
	ws_range = range(ws)
	grid = []

	# Combined till, plant and initial sort
	for x in ws_range:
		grid.append([])
		for y in ws_range:
			# Till and plant
			till()
			plant(Entities.Cactus)

			# Initial sort
			if measure(West) and measure(West) > measure():
				swap(West)
			if measure(South) and measure(South) > measure():
				swap(South)
			if measure(West) and measure(West) > measure():
				swap(West)
			if measure(South) and measure(South) > measure():
				swap(South)

			# Store the measure
			grid[x].append(measure())
			grid[x-1][y] = measure(West)
			grid[x][y-1] = measure(South)

			move(North)
		move(East)
	return grid
	