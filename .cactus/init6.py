init6()
def init6():
	ws_range = range(get_world_size())
	grid = {}
	grid[0] = {}
	grid[1] = {}
	grid[2] = {}
	grid[3] = {}
	grid[4] = {}
	grid[5] = {}
	grid[6] = {}
	grid[7] = {}
	grid[8] = {}
	grid[9] = {}
	clear()

	# Create the grid
	# for x in ws_range:
	# 	grid.append([])
	# 	gridx = grid[x]
	# 	for y in ws_range:
	# 		gridx.append(None)

	# till plant and sort
	current_function = cacti_move_0
	while current_function:
		current_function = current_function(grid)


	# for x in ws_range:
	# 	for y in ws_range:

	# 		if grid[x][y] != measure():
	# 			quick_print("Error: grid not sorted", grid[x][y], measure(), x, y)

	# 		move(North)
	# 	move(East)
	return grid
