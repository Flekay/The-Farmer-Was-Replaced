clear()
MOVES = generate_moves()
GRID_SIZE = get_world_size()**2
TREE_BOOL = True
companions = {}

# till and plant
for dir in MOVES:
	TREE_BOOL = not TREE_BOOL
	coords = (get_pos_x(), get_pos_y())
	if coords in companions:
		harvest()
		plant(companions.pop(coords))
	elif TREE_BOOL:
			plant(Entities.Tree)
			use_item(Items.Water)
			while get_companion()[0] == Entities.Carrot:
				plant(Entities.Tree)
				harvest()
			companion, pos = get_companion()
			companions[pos] = companion
	else:
		plant(Entities.Bush)
	move(dir)


while num_items(Items.Wood) < 1000000:
	for dir in MOVES:
		TREE_BOOL = not TREE_BOOL
		coords = (get_pos_x(), get_pos_y())
		if coords in companions:
			comp = companions.pop(coords)
			if get_entity_type() == comp:
				move(dir)
			else:
				harvest()
				plant(comp)
				move(dir)
		elif TREE_BOOL:
				while get_water() < 0.75:
					use_item(Items.Water)
				while not can_harvest():
					use_item(Items.Fertilizer)
				harvest()
				if num_items(Items.Wood) > 1000000:
					break
				plant(Entities.Tree)
				companion, pos = get_companion()
				companions[pos] = companion
				move(dir)
		else:
			plant(Entities.Bush)
			move(dir)
			