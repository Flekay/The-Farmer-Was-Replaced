def generate_moves_pos(ws=get_world_size()):
	moves = []
	rr1 = range(ws)
	rr2 = range(ws-1)
	pos_x = 0
	pos_y = 0
	for x in rr1:
		for y in rr2:
			moves.append((North, (pos_x, pos_y)))
			pos_y = (pos_y + 1) % ws
		moves.append((East, (pos_x, pos_y)))
		pos_x = (pos_x + 1) % ws
	return moves


MOVES = generate_moves_pos()
