# Initialize world size and variables
set_world_size(5)
# /movement/loop_around/map_pos.py
from map_pos import MOVES
companions = {}


while num_items(Items.Hay) < 100000:
	for dir, coords in MOVES:
		if coords in companions:
			comp = companions.pop(coords)
			if get_entity_type() == comp:
				move(dir)
			else:
				if get_entity_type() == Entities.Grass:
					while not can_harvest():
						continue
				harvest()
				plant(comp)
				move(dir)
		else:
			if get_entity_type() == Entities.Grass:
				while not can_harvest():
					continue
			harvest()
			companion, pos = get_companion()
			while companion == Entities.Carrot or (pos in companions and companion != companions[pos]):
				harvest()
				companion, pos = get_companion()
			companions[pos] = companion
			move(dir)
