# Visit each tile and plants a given entity.
#
# Arguments:
#	entity (entity): the entity to plant
#
# Example:
#	batch_plant(Entities.Carrot)
def batch_plant(entity):
	ws = get_world_size()
	MOVES = [East, North, North]
	for _ in range(ws-3):
		MOVES.append(North)
	for _ in MOVES:
		for direction in MOVES:
			plant(entity)
			move(direction)
