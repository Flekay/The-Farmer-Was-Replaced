# Recursive Depth-First Search (DFS) for Maze Exploration
# Recursively explores the maze starting with a move to the north. If moving north is successful,
# the function checks for the Treasure and saves its position if detected. After handling the northern
# direction, it recursively invokes scans for additional directions (north, east, and west) to perform
# a depth-first search (DFS) on adjacent paths. Once exploration in these directions is complete, it
# backtracks by moving south to return to the previous position.

treasure_position = None

def explore_north():
	global treasure_position
	# Attempt to move north
	if move(North):
		# If the move is successful, check for treasure
		if measure():
			# If treasure is found, save its position
			treasure_position = get_pos_x(), get_pos_y()

		# Recursively explore adjacent paths excluding the opposite direction (south)
		explore_north()
		explore_east()
		explore_west()

		# Backtrack to the previous position
		move(South)

def explore_east():
	global treasure_position
	if move(East):
		if measure():
			treasure_position = get_pos_x(), get_pos_y()
		explore_north()
		explore_east()
		explore_south()
		move(West)

def explore_south():
	global treasure_position
	if move(South):
		if measure():
			treasure_position = get_pos_x(), get_pos_y()
		explore_north()
		explore_east()
		explore_south()
		move(North)

def explore_west():
	global treasure_position
	if move(West):
		if measure():
			treasure_position = get_pos_x(), get_pos_y()
		explore_north()
		explore_east()
		explore_south()
		move(East)

if __name__ == "__main__":
	# Main function to initiate the maze exploration
	explore_north()
	explore_east()
	explore_south()
	explore_west()
