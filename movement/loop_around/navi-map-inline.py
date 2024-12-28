def generate_moves_inline(SIZE=get_world_size()):
	MOVES = [East, North, North]
	for _ in range(SIZE-3):
		MOVES.append(North)
	return MOVES
