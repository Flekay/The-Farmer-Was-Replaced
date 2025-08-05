# Initialize world size and variables
ws = 5
set_world_size(ws)
# /movement/loop_around/map_light.py
from map_light import MOVES
TINY_MOVES = (South, West, North, East)
BUSHES = set()
GRASSES = {(0,0), (4,0), (4,4), (0,4)}

# Plant everywhere except in the corners
for dir in MOVES:
	pos = (get_pos_x(), get_pos_y())
	if pos not in GRASSES:
		plant(Entities.Bush)
		BUSHES.add((Entities.Bush, pos))
	move(dir)

# Plant grass with correct companions
for dir in TINY_MOVES:
	while get_companion() not in BUSHES:
		harvest()
	use_item(Items.Water)
	move(dir)

# Main loop
# Harvest and replant grass in the corners
while num_items(Items.Hay) < 100000:
	for dir in TINY_MOVES:
		while not can_harvest():
			continue
		harvest()
		while get_companion() not in BUSHES:
			harvest()
		if get_water() < 0.85:
			use_item(Items.Water)
		move(dir)
