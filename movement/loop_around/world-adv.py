def generate_world_moves(
		n = get_world_size()**2,
		world_size = get_world_size(),
		pos_x = 0,
		pos_y = 0
	):
	moves = []
	if n > world_size**2:
		world_moves = generate_world_moves(world_size**2, world_size, pos_x, pos_y)
		for i in range(n // world_size**2):
			moves += world_moves
		n %= world_size**2

	if world_size % 2 == 0:
		for i in range(n):
			if pos_x == 0 and pos_y < world_size - 1:
				pos_y += 1
				moves.append(North)
			elif pos_y % 2 == 0 and pos_x != 1:
				pos_x -= 1
				moves.append(West)
			elif pos_y % 2 != 0 and pos_x != world_size - 1:
				pos_x += 1
				moves.append(East)
			elif pos_x == 1 and pos_y == 0:
				pos_x -= 1
				moves.append(West)
			else:
				pos_y -= 1
				moves.append(South)
	else:
		print("Odd world size not supported yet")
	return moves
