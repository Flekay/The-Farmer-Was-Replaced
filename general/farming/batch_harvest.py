# Visits all tiles and harvests them.
def batch_harvest():
	ws = get_world_size()
	MOVES = [East, North, North]
	for _ in range(ws-3):
		MOVES.append(North)
	for _ in MOVES:
		for direction in MOVES:
			harvest()
			move(direction)
