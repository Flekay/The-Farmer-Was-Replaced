def plant_and_sort(SIZE=get_world_size()):
	grid = {}
	for x in range(SIZE):
		grid[x] = {}
		for y in range(SIZE):
			till()
			plant(Entities.Cactus)
			simple_swaping()
			grid[x][y] = measure()
			if x:
				grid[x - 1][y] = measure(West)
			move(North)
		move(East)
	return grid


# swapping 2 rounds to ensure all cacti are sorted
# in this case, we don't need to swap East, because its always None
def simple_swaping():
	# First round of swaps
	if measure(West) and measure(West) > measure():
		swap(West)
	if measure(North) and measure(North) < measure():
		swap(North)
	if measure(South) and measure(South) > measure():
		swap(South)
	# if measure(East) and measure(East) < measure():
	# 	swap(East)

	# Second round of swaps
	if measure(West) and measure(West) > measure():
		swap(West)
	if measure(North) and measure(North) < measure():
		swap(North)
	if measure(South) and measure(South) > measure():
		swap(South)
	# if measure(East) and measure(East) < measure():
	# 	swap(East)
