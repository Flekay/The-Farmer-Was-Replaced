clear()
from map_pos import MOVES
companions = {}

for dir, coords in MOVES:
	till()
	if coords in companions:
		plant(companions.pop(coords))
		move(dir)
	else:
		plant(Entities.Carrot)
		companion, pos = get_companion()
		while pos in companions and companion != companions[pos]:
			harvest()
			plant(Entities.Carrot)
			companion, pos = get_companion()
		companions[pos] = companion
		move(dir)

while num_items(Items.Carrot) < 100000:
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
			if get_entity_type() == Entities.Carrot:
				while not can_harvest():
					if get_water() < 0.5:
						use_item(Items.Water)
					use_item(Items.Fertilizer)
			harvest()
			plant(Entities.Carrot)
			companion, pos = get_companion()
			while pos in companions and companion != companions[pos]:
				harvest()
				plant(Entities.Carrot)
				companion, pos = get_companion()
			companions[pos] = companion
			move(dir)
