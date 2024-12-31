clear()
MOVES = generate_moves()
GRID_SIZE = get_world_size()**2
TREE_BOOL = True
companions = {}

# till and plant
for dir in MOVES:
	TREE_BOOL = not TREE_BOOL
	if TREE_BOOL:
			plant(Entities.Tree)
	else:
		plant(Entities.Bush)
	move(dir)

