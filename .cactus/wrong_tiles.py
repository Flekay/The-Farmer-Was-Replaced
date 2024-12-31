
def wrong_tiles(grid=None):
	if grid == None:
		MOVES = generate_moves()
		grid = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}}
		for direction in MOVES:
			grid[get_pos_x()][get_pos_y()] = measure()
			move(direction)

	wrong_positions = []
	world_size = get_world_size()
	for y in range(world_size - 1, -1, -1):
		for x in range(world_size):
			current = grid[x][y]
			# Check North neighbor
			if y < world_size - 1 and grid[x][y + 1] < current:
				wrong_positions.append([x, y])
			# Check East neighbor
			if x < world_size - 1 and grid[x + 1][y] < current:
				wrong_positions.append([x, y])
			# Check South neighbor
			if y > 0 and grid[x][y - 1] > current:
				wrong_positions.append([x, y])
			# Check West neighbor
			if x > 0 and grid[x - 1][y] > current:
				wrong_positions.append([x, y])
	return wrong_positions
