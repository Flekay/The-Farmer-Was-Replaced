def simple_swaping():
	current_measure = measure()
	west_measure = measure(West)
	north_measure = measure(North)
	south_measure = measure(South)
	east_measure = measure(East)
	temp_measure = None
	swapped = False
	if north_measure < current_measure and swap(North):
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swapped = True
	if south_measure > current_measure and swap(South):
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swapped = True
	if west_measure > current_measure and swap(West):
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		swapped = True
	if east_measure < current_measure and swap(East):
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		swapped = True
	if swapped:
		if north_measure < current_measure and swap(North):
			temp_measure = north_measure
			north_measure = current_measure
			current_measure = temp_measure
		if south_measure > current_measure and swap(South):
			temp_measure = south_measure
			south_measure = current_measure
			current_measure = temp_measure
		if west_measure > current_measure and swap(West):
			temp_measure = west_measure
			west_measure = current_measure
			current_measure = temp_measure
		if east_measure < current_measure and swap(East):
			temp_measure = east_measure
			east_measure = current_measure
			current_measure = temp_measure
	return swapped




def naive_bubble_sort(grid=None):
	moves_north = [North, North]
	for _ in range(get_world_size()-3):
		moves_north.append(North)
	moves = list()
	for _ in range(get_world_size()):
		moves += moves_north
		moves.append(East)

	unfinished = True
	while unfinished:
		unfinished = False
		simple_swaping()
		for dir in moves:
			move(dir)
			if simple_swaping():
				unfinished = True
