
def init3():
	ws_range = range(get_world_size())
	grid = []
	clear()

	# time = get_time()
	# till plant and sort
	current_function = cacti_move_0
	while current_function:
		current_function = current_function()
	# quick_print("planting",get_time()-time)
	
	#time = get_time()
	# measure and sort
	for x in ws_range:
		grid.append([])
		for y in ws_range:

			# Initial sort
			simple_swap()

			# Store the measure
			grid[x].append(measure())
			grid[x-1][y] = measure(West)
			grid[x][y-1] = measure(South)

			move(North)
		move(East)
	#quick_print("measure",get_time()-time)
	return grid
	