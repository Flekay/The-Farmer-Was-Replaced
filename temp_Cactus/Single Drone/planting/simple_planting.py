def simple_planting(SIZE=get_world_size()):
	grid = {}
	for x in range(SIZE):
		grid[x] = {}
		for y in range(SIZE):
			till()
			plant(Entities.Cactus)
			grid[x][y] = measure()
			move(North)
		move(East)
	return grid
