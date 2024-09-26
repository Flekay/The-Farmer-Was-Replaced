def almighty(ws = get_world_size()):
	path = []

	def stack(width):
		STACK = []
		for _ in range(width):
			STACK.append(East)
		STACK.append(South)
		for _ in range(width):
			STACK.append(West)
		return STACK

	def zigzag(width):
		even = [North, West]
		odd = [South, West]
		ZIGZAG = []
		for i in range(width):
			if i % 2:
				ZIGZAG += odd
			else:
				ZIGZAG += even
		return ZIGZAG

	STACK = stack(ws - 2)
	if ws % 2:
		shared_path = []
		path1 = []
		path2 = []
		for _ in range(ws - 2):
			shared_path.append(North)
		shared_path.append(East)
		for _ in range(ws // 2 - 1):
			shared_path += STACK
			shared_path.append(South)
		for _ in range(ws - 2):
			shared_path.append(East)
		shared_path += [South, South, West]
		shared_path += zigzag(ws - 3)

		path1 = [North] + shared_path + [North, West]
		path2 = shared_path + [West]
		path = path1 + path2
	else:
		for _ in range(ws - 1):
			path.append(North)
		path.append(East)
		for _ in range(ws // 2 - 1):
			path += STACK
			path.append(South)
		path += STACK
		path.append(West)

	return path

def allmighty_offset(path, new_start_pos):
	# Follow the path until reaching the desired position
	current_x, current_y = 0, 0
	DIRECTIONS = {North: (0, 1), South: (0, -1), East: (1, 0), West: (-1, 0)}
	moved_path = []
	remaining_path = list(path)

	for direction in path:
		current_x += DIRECTIONS[direction][0]
		current_y += DIRECTIONS[direction][1]
		moved_path.append(remaining_path.pop(0))
		if (current_x, current_y) == new_start_pos:
			break

	# Append the moved part to the end of the remaining path
	return remaining_path + moved_path

clear()
MOVES = almighty()
change_hat(Hats.Dinosaur_Hat)
while True:
	for dir in MOVES:
		if not move(dir):
			change_hat(Hats.Dinosaur_Hat)
