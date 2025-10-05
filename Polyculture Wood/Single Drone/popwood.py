from map_pos import MOVES
companions = {}
flipflop = True

def plant_tree():
	global companions
	plant(Entities.Tree)
	companion, pos = get_companion()
	x, y = pos
	while companion == Entities.Carrot or (pos in companions and companion != companions[pos]):
		harvest()
		plant(Entities.Tree)
		companion, pos = get_companion()
		x, y = pos
	companions[pos] = companion

def handle_grass():
	plant_tree()
	if not get_water():
		use_item(Items.Water)

def handle_bush():
	harvest()
	plant_tree()
	if not get_water():
		use_item(Items.Water)

def handle_tree():
	global companions
	if can_harvest():
		harvest()
		plant_tree()
		if not get_water():
			use_item(Items.Water)
	else:
		if get_water() and use_item(Items.Fertilizer):
			use_item(Items.Weird_Substance)
			if can_harvest():
				harvest()
				plant_tree()
				if not get_water():
					use_item(Items.Water)
		else:
			companion, pos = get_companion()
			companions[pos] = companion

handles = {
	Entities.Grass: handle_grass,
	Entities.Bush: handle_bush,
	Entities.Tree: handle_tree
}

while num_items(Items.Wood) < 100000:
	for dir, coords in MOVES:
		# Companion
		if coords in companions:
			comp = companions.pop(coords)
			entity_type = get_entity_type()
			if entity_type != comp:
				if entity_type != Entities.Grass:
					if entity_type == Entities.Tree and get_water():
						if use_item(Items.Fertilizer):
							while not can_harvest():
								continue
					harvest()
				if comp != Entities.Grass:
					plant(comp)
		# Tree
		elif flipflop:
			handles[get_entity_type()]()
		flipflop = not flipflop
		move(dir)
