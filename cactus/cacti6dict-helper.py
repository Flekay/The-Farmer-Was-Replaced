# Function to check if a combination is valid
def is_valid_combination(combination):
	encountered_none = False
	for state in combination:
		if encountered_none and state != None:
			return False
		if state == None:
			encountered_none = True
	return True

# Function to build the dictionary with grid combinations and their swap orders
def build_grid_dict():
	possible_states = list(range(10))
	all_states = [None] + list(range(10))
	grid_dict = {}
	for state0 in possible_states:
		for state1 in all_states:
			for state2 in all_states:
				for state3 in all_states:
					combination = (state0, state1, state2, state3)
					if is_valid_combination(combination):
						optimal_swap_order = calculate_optimal_swap_order(combination)
						grid_dict[combination] = optimal_swap_order
	return grid_dict

# Function to calculate the optimal swap order
def calculate_optimal_swap_order(comb):
	north = None
	east = None
	south = None
	player = comb[0]
	available_positions = [North, East, South]
	swap_1 = []
	swap_2 = []
	swap_3 = []
	# Determine initial swap direction based on the first element
	if comb[0] in {0, 1, 2}:
		south, player = player, comb[1]
		swap_1.append(South)
		available_positions.remove(South)
	elif comb[0] in {7, 8, 9}:
		east, player = player, comb[1]
		swap_1.append(East)
		available_positions.remove(East)
	else:
		north, player = player, comb[1]
		swap_1.append(North)
		available_positions.remove(North)
	
	# second element
	if comb[1] != None:
		if comb[1] in {7, 8, 9}:
			if East in available_positions:
				east, player = player, comb[2]
				swap_2.append(East)
				available_positions.remove(East)
			else:
				north, player = player, comb[2]
				swap_2.append(North)
				available_positions.remove(North)
		elif comb[1] in {0, 1, 2}:
			if South in available_positions:
				south, player = player, comb[2]
				swap_2.append(South)
				available_positions.remove(South)
			else:
				north, player = player, comb[2]
				swap_2.append(North)
				available_positions.remove(North)
		else:
			if available_positions[0] == North:
				north, player = player, comb[2]
			elif available_positions[0] == East:
				east, player = player, comb[2]
			else:
				south, player = player, comb[2]
				
			swap_2.append(available_positions[0])
			available_positions.remove(available_positions[0])
	else:
		return swap_1[0]
	
	# third element
	if comb[2] != None:
		if available_positions[0] == North:
			north, player = player, comb[3]
		elif available_positions[0] == East:
			east, player = player, comb[3]
		else:
			south, player = player, comb[3]
			
		swap_3.append(available_positions[0])
		# available_positions.remove(available_positions[0])
	else:
		return swap_2[0]
	
	# fourth element
	if comb[3] == None:
		return swap_3[0]
	
	# final swapping
	return final_swaps(north, east, south, player)

# Function to determine the final swaps with minimal swaps
def final_swaps(north, east, south, player):
	swaps = []

	if north < player:
		swaps.append(North)
		player, north = north, player

	if east < player:
		swaps.append(East)
		player, east = east, player

	if south > player:
		swaps.append(South)
		player, south = south, player
		
	if north < player:
		swaps.append(North)
		player, north = north, player

	if east < player:
		swaps.append(East)
		player, east = east, player

	return swaps
















# Function to build the dictionary with grid combinations and their swap orders
def build_grid_dict2():
	all_states = list(range(10))
	grid_dict = {}
	for state0 in all_states:
		for state1 in all_states:
			for state2 in all_states:
				for state3 in all_states:
					grid_dict[(state0, state1, state2, state3)] = final_swaps_2(state0, state1, state2, state3)
	return grid_dict


# Function to determine the final swaps with minimal swaps
def final_swaps_2(north, east, west, player):
	swaps = []

	if north < player:
		swaps.append(North)
		player, north = north, player

	if east < player:
		swaps.append(East)
		player, east = east, player

	if west > player:
		swaps.append(West)
		player, west = west, player
		
	if north < player:
		swaps.append(North)
		player, north = north, player

	if east < player:
		swaps.append(East)
		player, east = east, player

	return swaps