def generate_moves(
		n = get_world_size()**2,
		world_size = get_world_size(),
		pos_x = 0,
		pos_y = 0
	):
	
	moves = []
	for i in range(n):
		if pos_x % world_size == pos_y % world_size:
			pos_x -= 1
			moves.append(West)
		else:
			pos_y += 1
			moves.append(North)
	return moves