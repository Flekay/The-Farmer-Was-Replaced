import os

world_size = 10
ALMIGHTY = [
	"North", "East", "East", "North", "West", "West", "North", "East", "East", "North",
	"West", "West", "North", "East", "East", "East", "East", "North", "West", "West",
	"West", "West", "North", "North", "North", "East", "South", "South", "East", "North",
	"North", "East", "South", "South", "East", "North", "North", "East", "South", "South",
	"South", "South", "East", "North", "North", "North", "North", "East", "East", "East",
	"South", "West", "West", "South", "East", "East", "South", "West", "West", "South",
	"East", "East", "South", "West", "West", "West", "West", "South", "East", "East",
	"East", "East", "South", "South", "South", "West", "North", "North", "West", "South",
	"South", "West", "North", "North", "West", "South", "South", "West", "North", "North",
	"North", "North", "West", "South", "South", "South", "South", "West", "West", "West"
]
OOP = {
	"North": "South",
	"South": "North",
	"East": "West",
	"West": "East"
}

def create_position_index_map(directions):
	# Direction mapping
	moves = {
		"North": (0, 1),
		"South": (0, -1),
		"East": (1, 0),
		"West": (-1, 0)
	}

	# Initialize
	pos = (0, 0)
	pos_index_map = {pos: 0}  # Starting position
	i = 0

	# Track each position
	for direction in directions[:-1]:
		i += 1
		# Update position based on direction
		dx, dy = moves[direction]
		pos = (pos[0] + dx, pos[1] + dy)

		# Store position and index
		pos_index_map[pos] = i

	return pos_index_map

# Example usage
position_map = create_position_index_map(ALMIGHTY)
center_tiles = [
	(3, 3), (4, 3), (5, 3), (6, 3),
	(3, 4), (4, 4), (5, 4), (6, 4),
	(3, 5), (4, 5), (5, 5), (6, 5),
	(3, 6), (4, 6), (5, 6), (6, 6)
]
center_tiles = []

# center_tiles = [
# 	(4, 4), (5, 4),
# 	(4, 5), (5, 5),
# ]
# print(position_map)
# {(0, 0): 0, (0, 1): 1, (1, 1): 2, (2, 1): 3, (2, 2): 4, (1, 2): 5, (0, 2): 6, (0, 3): 7, (1, 3): 8, (2, 3): 9, (2, 4): 10, (1, 4): 11, (0, 4): 12, (0, 5): 13, (1, 5): 14, (2, 5): 15, (3, 5): 16, (4, 5): 17, (4, 6): 18, (3, 6): 19, (2, 6): 20, (1, 6): 21, (0, 6): 22, (0, 7): 23, (0, 8): 24, (0, 9): 25, (1, 9): 26, (1, 8): 27, (1, 7): 28, (2, 7): 29, (2, 8): 30, (2, 9): 31, (3, 9): 32, (3, 8): 33, (3, 7): 34, (4, 7): 35, (4, 8): 36, (4, 9): 37, (5, 9): 38, (5, 8): 39, (5, 7): 40, (5, 6): 41, (5, 5): 42, (6, 5): 43, (6, 6): 44, (6, 7): 45, (6, 8): 46, (6, 9): 47, (7, 9): 48, (8, 9): 49, (9, 9): 50, (9, 8): 51, (8, 8): 52, (7, 8): 53, (7, 7): 54, (8, 7): 55, (9, 7): 56, (9, 6): 57, (8, 6): 58, (7, 6): 59, (7, 5): 60, (8, 5): 61, (9, 5): 62, (9, 4): 63, (8, 4): 64, (7, 4): 65, (6, 4): 66, (5, 4): 67, (5, 3): 68, (6, 3): 69, (7, 3): 70, (8, 3): 71, (9, 3): 72, (9, 2): 73, (9, 1): 74, (9, 0): 75, (8, 0): 76, (8, 1): 77, (8, 2): 78, (7, 2): 79, (7, 1): 80, (7, 0): 81, (6, 0): 82, (6, 1): 83, (6, 2): 84, (5, 2): 85, (5, 1): 86, (5, 0): 87, (4, 0): 88, (4, 1): 89, (4, 2): 90, (4, 3): 91, (4, 4): 92, (3, 4): 93, (3, 3): 94, (3, 2): 95, (3, 1): 96, (3, 0): 97, (2, 0): 98, (1, 0): 99}


# def x0y0(goal_idx):
#     move(North)
#     return x0y1

# def x0y1(goal_idx):
#     ...

def get_neighbours(pos, idx):
	listed = []
	x, y = pos
	if x > 0:
		listed.append((x - 1, y))
	if x < world_size - 1:
		listed.append((x + 1, y))
	if y > 0:
		listed.append((x, y - 1))
	if y < world_size - 1:
		listed.append((x, y + 1))
	return listed


def path_distance(pos1_idx, pos2_idx):
	return abs(pos2_idx - pos1_idx)

def get_possible_moves(pos, world_size):
	x, y = pos
	moves = []
	for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
		new_x, new_y = x + dx, y + dy
		if 0 <= new_x < world_size and 0 <= new_y < world_size:
			moves.append((new_x, new_y))
	return moves


def generate_state_machine(position_map, output_file):
	moves = {
		"North": (0, 1),
		"South": (0, -1),
		"East": (1, 0),
		"West": (-1, 0)
	}

	functions = []
	for pos in position_map:
		idx = position_map[pos]
		curr_func = f"SMx{pos[0]}y{pos[1]}a"

		# Default path
		direction = ALMIGHTY[idx]
		next_pos = (pos[0] + moves[direction][0], pos[1] + moves[direction][1])
		next_func = f"SMx{next_pos[0]}y{next_pos[1]}a"

		# Check for possible shortcuts
		shortcut_checks = []
		for next_pos in get_possible_moves(pos, world_size):
			if next_pos in position_map:
				next_idx = position_map[next_pos]
				move_direction = "East" if next_pos[0] > pos[0] else "West" if next_pos[0] < pos[0] else "North" if next_pos[1] > pos[1] else "South"
				if move_direction != direction and move_direction != OOP[ALMIGHTY[idx-1]] and next_pos not in center_tiles:
					shortcut_checks.append(
						f"\tif (path_distance({next_idx}, goal_idx) < default_distance) and move({move_direction}):"
						# f"\tif dist <= cuttingAmountAvailable and move({move_direction}):"
						# f"\tif path_distance({idx}, {next_idx}) <= cutting_amount:"
						# f"\n\t\tmove({move_direction})"
						f"\n\t\treturn SMx{next_pos[0]}y{next_pos[1]}a"
					)
			else:
				print(f"Position {next_pos} not in position map")

		# Write function with shortcuts
		# functions.append(f"def {curr_func}(goal_idx):")
		functions.append(f"def {curr_func}(goal_idx, length, snake_body, position_function_dict):")
		# debug
		# functions.append(f"\tif (get_pos_x(), get_pos_y()) != {pos}:")
		# functions.append(f"\t\t[]=[[],[]]")
		# functions.append(f"\tsnake_body.append({pos})")
		if shortcut_checks:
			# functions.append(f"\ttail_distance = path_distance({idx}, position_function_dict[snake_body[0]])")
			# functions.append(f"\tfood_distance = path_distance({idx}, goal_idx)")
			# functions.append(f"\tcutting_amount = tail_distance - length")
			# functions.append(f"\tif food_distance < cutting_amount:")
			# functions.append(f"\t\tcutting_amount = food_distance")
				# if(tfood_distance < tcutting_amount)
				# 	tcutting_amount = tfood_distance;
				# if(tcutting_amount < 0)
				# 	tcutting_amount = 0;
			functions.append(f"\tdefault_distance = path_distance({idx}, goal_idx)")
			functions.extend(shortcut_checks)
		functions.append(f"\tmove({direction})")
		functions.append(f"\treturn {next_func}")

	# Write to file
	total_positions = world_size ** 2
	with open(os.path.join(os.path.dirname(__file__), output_file), "w") as f:
		# f.write(f"def path_distance(pos1_idx, pos2_idx, total_positions={total_positions}):\n")
		# f.write("\treturn (pos2_idx - pos1_idx) % total_positions\n\n")
		f.write("\n".join(functions))

generate_state_machine(position_map, "state_machine.py")
