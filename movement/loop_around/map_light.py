def generate_moves_light(ws=get_world_size()):
	moves_north = [North, North]
	for _ in range(ws-3):
		moves_north.append(North)
	moves = list()
	for _ in range(ws):
		moves += moves_north
		moves.append(East)
	return moves

MOVES = generate_moves_light()
