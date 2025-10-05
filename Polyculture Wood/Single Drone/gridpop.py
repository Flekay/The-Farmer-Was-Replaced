MOVES = (North,North,North,North,East)
EVENODD = (True, False, True, False, True, False, True, False, True, False)
companions = {}

def plant_tree():
	global companions
	plant(Entities.Tree)
	companion, pos = get_companion()
	x, y = pos
	while companion == Entities.Carrot or EVENODD[x-y] or (pos in companions and companion != companions[pos]):
		harvest()
		plant(Entities.Tree)
		companion, pos = get_companion()
		x, y = pos
	companions[pos] = companion

while num_items(Items.Wood) < 100000:
	for dir in MOVES:
		# Tree
		if can_harvest():
			harvest()
			plant_tree()
			if not get_water():
				use_item(Items.Water)
		else:
			if use_item(Items.Fertilizer):
				use_item(Items.Weird_Substance)
				if can_harvest():
					harvest()
					plant_tree()
					if not get_water():
						use_item(Items.Water)
			else:
				companion, pos = get_companion()
				companions[pos] = companion
		move(dir)

		# Companion
		coords = (get_pos_x(), get_pos_y())
		if coords in companions:
			comp = companions.pop(coords)
			entity_type = get_entity_type()
			if entity_type != comp:
				if entity_type != Entities.Grass:
					harvest()
				if comp != Entities.Grass:
					plant(comp)
		move(North)
