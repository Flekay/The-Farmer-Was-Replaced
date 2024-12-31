def final3(grid):
	world_size = get_world_size()

	def wrong_tiles():
		wrong_positions = []
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

	# quick_print(wrong_tiles())

	# manhatten distance on a self wrapping 10x10 grid
	def mandistance(point1, point2):
		dx = abs(point1[0] - point2[0])
		dy = abs(point1[1] - point2[1])
		return min(dx, world_size - dx) + min(dy, world_size - dy)

	def nearest_neighbor(start_pos, positions):
		min_distance = 999
		nearest_pos = None
		for pos in positions:
			distance = mandistance(start_pos, pos)
			if distance < min_distance:
				min_distance = distance
				nearest_pos = pos
		positions.remove(nearest_pos)
		return nearest_pos

	tiles = wrong_tiles()
	(x,y) = nearest_neighbor((0,0), tiles)
	move_to(x,y)
	simple_swap()
	while tiles:
		(x,y) = nearest_neighbor((x,y), tiles)
		move_to(x,y)
		simple_swap()

	harvest()
	