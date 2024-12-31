def generate_moves(
		n = get_world_size()**2,
		world_size = get_world_size(),
		pos_x = 0,
		pos_y = 0
	):
	moves = []
	if n > world_size**2:
		world_moves = generate_moves(world_size**2, world_size, pos_x, pos_y)
		for i in range(n // world_size**2):
			moves += world_moves
		n %= world_size**2

	for i in range(n):
		if pos_x % world_size == pos_y % world_size:
			pos_x -= 1
			moves.append(West)
		else:
			pos_y += 1
			moves.append(North)
	return moves
	
def generate_moves_light(ws=get_world_size()):
	moves_north = [North, North]
	for _ in range(ws-3):
		moves_north.append(North)
	moves = list()
	for _ in range(ws):
		moves += moves_north
		moves.append(East)
	return moves
	
def generate_small_moves():
	moves = [East]
	right_moves = []
	for _ in range(8):
		right_moves.append(East)
	right_moves.append(North)
	left_moves = []
	for _ in range(8):
		left_moves.append(West)
	left_moves.append(North)
	for _ in range(4):
		moves += right_moves
		moves += left_moves
	moves += right_moves
	moves[-1] = East
	for _ in range(8):
		moves.append(South)
	return moves