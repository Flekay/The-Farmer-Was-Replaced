EVENODD = (True, False, True, False, True, False, True, False, True, False)
MOVES = (North,North,North,North,East)
companions = {}

def plant_carrot():
	global companions
	plant(Entities.Carrot)
	companion, pos = get_companion()
	x, y = pos
	while EVENODD[x-y] or (pos in companions and companion != companions[pos]):
		harvest()
		plant(Entities.Carrot)
		companion, pos = get_companion()
		x, y = pos
	companions[pos] = companion

for _ in range(10):
	for dir in MOVES:
		# carrots
		till()
		plant_carrot()
		use_item(Items.Water)
		move(dir)

		# companions
		coords = get_pos_x(), get_pos_y()
		if coords in companions:
			comp = companions.pop(coords)
			if comp != Entities.Grass:
				plant(comp)
		move(North)

while num_items(Items.Carrot) < 100000:
	for dir in MOVES:
		# carrots
		if not can_harvest():
			if get_water() and use_item(Items.Fertilizer):
				use_item(Items.Weird_Substance)
				harvest()
			else:
				companion, pos = get_companion()
				companions[pos] = companion
		else:
			harvest()

		plant_carrot()
		if get_water() < 0.19:
			use_item(Items.Water)
		move(dir)

		# companions
		coords = get_pos_x(), get_pos_y()
		if coords in companions:
			comp = companions.pop(coords)
			entity_type = get_entity_type()
			if entity_type != comp:
				if entity_type != Entities.Grass:
					harvest()
				if comp != Entities.Grass:
					plant(comp)
		move(North)
