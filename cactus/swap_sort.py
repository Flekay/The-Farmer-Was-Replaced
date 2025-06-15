def simple_swaping():
	current_measure = measure()
	west_measure = measure(West)
	north_measure = measure(North)
	south_measure = measure(South)
	east_measure = measure(East)
	pos_x = get_pos_x()
	pos_y = get_pos_y()
	ws = get_world_size() - 1
	temp_measure = None
	swapped = False
	if west_measure > current_measure and pos_x > 0:
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		if swap(West):
			swapped = True
	if north_measure < current_measure and pos_y < ws:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		if swap(North):
			swapped = True
	if south_measure > current_measure and pos_y > 0:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		if swap(South):
			swapped = True
	if east_measure < current_measure and pos_x < ws:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		if swap(East):
			swapped = True
	if west_measure > current_measure and pos_x > 0:
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		if swap(West):
			swapped = True
	if north_measure < current_measure and pos_y < ws:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		if swap(North):
			swapped = True
	if south_measure > current_measure and pos_y > 0:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		if swap(South):
			swapped = True
	if east_measure < current_measure and pos_x < ws:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		if swap(East):
			swapped = True
	return swapped
