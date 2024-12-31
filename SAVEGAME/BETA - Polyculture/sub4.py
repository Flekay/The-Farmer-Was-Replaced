clear()
MOVES = generate_moves()
companions = {}
contin = True
TREE_GRID_POS = {}
for x in range(get_world_size()):
	for y in range(get_world_size()):
		TREE_GRID_POS[(x, y)] = (x + y) % 2

# get hay
for dir in MOVES:
	coords = (get_pos_x(), get_pos_y())
	if coords in companions:
		plant(companions.pop(coords))
		use_item(Items.Water)
		move(dir)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, pos = get_companion()
		companions[pos] = companion
		move(dir)

#get wood
for dir in MOVES:
	coords = (get_pos_x(), get_pos_y())
	if coords in companions:
		if get_entity_type() == companions[coords]:
			move(dir)
		else:
			harvest()
			if get_ground_type() == Grounds.Grassland:
				use_item(Items.Water)
				till()
			plant(companions.pop(coords))
			move(dir)
	else:

		harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
			use_item(Items.Water)
		if TREE_GRID_POS[coords]:
			move(dir)
		else:
			plant(Entities.Tree)
			companion, pos = get_companion()
			companions[pos] = companion
			move(dir)

# get carrots
while num_items(Items.Carrot) < 100000:
	for dir in MOVES:
		harvest()
		if get_water() < 0.5:
			use_item(Items.Water)
			use_item(Items.Water)
		if get_ground_type() == Grounds.Grassland:
			till()
		coords = (get_pos_x(), get_pos_y())
		if coords in companions:
			comp = companions.pop(coords)
			plant(comp)
		else:
			plant(Entities.Grass)
		companion, pos = get_companion()
		companions[pos] = companion
		move(dir)
		