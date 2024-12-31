
def init1():
	ws = get_world_size()
	ws_range = range(ws)
	grid = []
	moves = [
		North,East,North,East,North,East,North,East,North,East,
		North,East,North,East,North,North,North,North,North,North,
		North,North,North,West,West,South,West,South,West,South,
		West,South,West,South,East,East,North,East,East,North,
		East,North,North,North,North,North,West,South,West,South,
		West,South,South,West,North,North,North,North,East,East,
		South,West,South,West,West,South,South,South,East,East,
		South,West,South,East,East,East,North,East,North,West,
		North,North,North,North,North,North,North,North,East,
		South,South,South,East,East,South,South,South,South,West,
		South,East,South,South,West,North,West,West,West,South,
		West,South,South,East,North,East,South,East,East,North,
		East,East,East,South,South,East,South,South,South,East,
		East,North,North,North,East,South,South,South,South,West,
		West,North,North,North,North,North,North,North,West,North,
		West,West,West,North,North,North,West,West,South,West,South,
	]

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
			# l[x].append(measure())
			# l[x-1][y] = measure(West)
			# l[x][y-1] = measure(South)

			move(North)
		move(East)

	for dir in moves:
		move(dir)
		simple_swap()

	# quick debug scan
	# ticks = get_tick_count()
	move_to(0, 0)
	for x in ws_range:
		for y in ws_range:
			# grid[get_pos_x()][get_pos_y()] = measure()
			grid[x].append(measure())
			move(North)
		move(East)
	# quick_print("debu",get_tick_count() - ticks)
	return grid
	