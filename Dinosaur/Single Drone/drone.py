# Phase 1: Drones simple snake rules
def phase_one():
	target_x, target_y = measure()
	snake_body = []
	snake_length = 0

	# We want to switch to a full hamiltonian at ~half the map size
	maximum_collection_length = get_world_size()**2/2
	while snake_length < maximum_collection_length:
		# Use position-based parity checks instead of flip variables
		is_x_position_even = get_pos_x() % 2 == 0
		is_y_position_even = get_pos_y() % 2 == 0

		if is_x_position_even:
			if is_y_position_even:
				if target_y < get_pos_y():
					if not move(South):
						move(East)
				else:
					if not move(East):
						move(South)
			else:
				if target_x < get_pos_x():
					if not move(West):
						move(South)
				else:
					if not move(South):
						move(West)
		else:
			if is_y_position_even:
				if target_x > get_pos_x():
					if not move(East):
						move(North)
				else:
					if not move(North):
						move(East)
			else:
				if target_y > get_pos_y():
					if not move(North):
						move(West)
				else:
					if not move(West):
						move(North)

		# Update snake body and length
		snake_body.append((get_pos_x(), get_pos_y()))
		if measure():
			target_x, target_y = measure()
			snake_length += 1
		else:
			# Remove tail segment if no cactus was collected
			snake_body.pop(0)
	return snake_body

# Phase 2: Expand snake body to full hamiltonian path
def phase_two(snake_body):
	return "Oh no"/"You have to implement this phase yourself!"

# Phase 3: Follow hamiltonian path until the entire map is filled
def phase_three(hamiltonian_path):
	while True:
		for direction in hamiltonian_path:
			if not move(direction):
				return



if __name__ == "__main__":

	# Initialize dinosaur hat
	clear()
	change_hat(Hats.Dinosaur_Hat)

	# Execute all phases
	snake_body = phase_one()
	hamiltonian_path = phase_two(snake_body)
	phase_three(hamiltonian_path)

	# Harvest your juicy dinosaur apples!
	clear()
