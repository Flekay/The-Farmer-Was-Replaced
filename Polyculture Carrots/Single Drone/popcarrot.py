clear()
MOVES = (North,North,North,North,North,North,North,North,North,East)
companions = {}

def plant_carrot():
	global companions
	plant(Entities.Carrot)
	companion, pos = get_companion()
	while (pos in companions and companion != companions[pos]):
		harvest()
		plant(Entities.Carrot)
		companion, pos = get_companion()
	companions[pos] = companion

def handle_grass():
	plant_carrot()
	if not get_water():
		use_item(Items.Water)

def handle_bush():
	harvest()
	plant_carrot()
	if not get_water():
		use_item(Items.Water)

def handle_tree():
	harvest()
	plant_carrot()
	if not get_water():
		use_item(Items.Water)

def handle_carrot():
	global companions
	if can_harvest():
		harvest()
		plant_carrot()
		if not get_water():
			use_item(Items.Water)
	else:
		if get_water() and use_item(Items.Fertilizer):
			use_item(Items.Weird_Substance)
			if can_harvest():
				harvest()
				plant_carrot()
				if not get_water():
					use_item(Items.Water)
		else:
			companion, pos = get_companion()
			companions[pos] = companion

handles = {
	Entities.Grass: handle_grass,
	Entities.Bush: handle_bush,
	Entities.Tree: handle_tree,
	Entities.Carrot: handle_carrot
}

for _ in range(10):
	for dir in MOVES:
		coords = (get_pos_x(), get_pos_y())
		till()
		if coords in companions:
			plant(companions.pop(coords))
		else:
			plant_carrot()
			use_item(Items.Water)
		move(dir)

while num_items(Items.Carrot) < 100000:
	for dir in MOVES:
		coords = (get_pos_x(), get_pos_y())
		if coords in companions:
			comp = companions.pop(coords)
			entity_type = get_entity_type()
			if entity_type != comp:
				if entity_type != Entities.Grass:
					if entity_type == Entities.Carrot:
						while not can_harvest():
							use_item(Items.Fertilizer)
					harvest()
				plant(comp)
		else:
			handles[get_entity_type()]()
		move(dir)
		