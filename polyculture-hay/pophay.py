set_world_size(5)
from map_pos import MOVES
companions = {}

# first loop does not need to be harvested
for dir, coords in MOVES:
	if coords in companions:
		plant(companions.pop(coords))
		move(dir)
	else:
		companion, pos = get_companion()
		while companion == Entities.Carrot or (pos in companions and companion != companions[pos]):
			harvest()
			companion, pos = get_companion()
		companions[pos] = companion
		move(dir)

# main loop
for _ in range(34):
	for dir, coords in MOVES:
		if coords in companions:
			comp = companions.pop(coords)
			if get_entity_type() == comp:
				move(dir)
			else:
				harvest()
				plant(comp)
				move(dir)
		else:
			harvest()
			companion, pos = get_companion()
			while companion == Entities.Carrot or (pos in companions and companion != companions[pos]):
				harvest()
				companion, pos = get_companion()
			companions[pos] = companion
			move(dir)

# Last few loops to ensure at least 99250 hay
while num_items(Items.Hay) < 99250:
	for dir, coords in MOVES:
		if coords in companions:
			comp = companions.pop(coords)
			if get_entity_type() == comp:
				move(dir)
			else:
				harvest()
				plant(comp)
				move(dir)
		else:
			harvest()
			if num_items(Items.Hay) > 99250:
				break
			companion, pos = get_companion()
			while companion == Entities.Carrot or (pos in companions and companion != companions[pos]):
				harvest()
				companion, pos = get_companion()
			companions[pos] = companion
			move(dir)

# guaranteed to harvest at least 750 hay
for dir, coords in MOVES:
	if get_entity_type() == Entities.Grass:
		harvest()
		if num_items(Items.Hay) > 100000:
			break
	move(dir)
	