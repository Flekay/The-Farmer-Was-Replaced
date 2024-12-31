
init5()
def init5():
	moves = [
		North, East, North, East, North, East, North, East, North, East,
		North, East, North, East, North, East, North, East, West, West,
		South, West, South, West, South, West, South, West, South, West,
		South, West, South, West, South, North, North, East, North, East,
		North, East, North, East, North, East, North, East, North, East,
		West, West, South, West, South, West, South, West, South, West,
		South, West, South, North, North, East, North, East, North, East,
		North, East, North, East, West, West, South, West, South, West,
		South, West, South, North, North, East, North, East, North, East,
		West, West, South, West, South, North, North, East, West, West,
		South, West, South, West, South, West, South, West, South, West,
		South, West, South, West, South, West, South, West, East, East,
		North, East, North, East, North, East, North, East, North, East,
		North, East, North, East, North, South, South, West, South, West,
		South, West, South, West, South, West, South, West, South, West,
		East, East, North, East, North, East, North, East, North, East,
		North, East, North, South, South, West, South, West, South, West,
		South, West, South, West, East, East, North, East, North, East,
		North, East, North, South, South, West, South, West, South, West,
		East, East, North, East, North, South, South, West, East, East,
	]
	# Create the grid
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
	# till plant and sort
	current_function = cacti2_move_0
	while current_function:
		current_function = current_function(grid)

	#move(West)
	#move(West)
	#move(North)
	# measure and sort
	for dir in moves:
		move(dir)
		simple_swap()
	#harvest()
	return grid
	