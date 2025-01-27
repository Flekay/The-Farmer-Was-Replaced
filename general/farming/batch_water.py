# Visits all tiles and waters them to a certain threshold.
def batch_water(threshold=0.5):
	ws = get_world_size()
	MOVES = [East, North, North]
	for _ in range(ws-3):
		MOVES.append(North)
	for _ in MOVES:
		for direction in MOVES:
			use_item(Item.Water)
			move(direction)
