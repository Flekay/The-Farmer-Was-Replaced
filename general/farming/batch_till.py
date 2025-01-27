# Visits all tiles and tills them.
def batch_till():
	ws = get_world_size()
	MOVES = [East, North, North]
	for _ in range(ws-3):
		MOVES.append(North)
	for _ in MOVES:
		for direction in MOVES:
			till()
			move(direction)
