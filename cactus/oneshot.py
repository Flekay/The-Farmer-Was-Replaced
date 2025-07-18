from map_inline import MOVES # movement/loop_aroud/map_inline.py
OOP = {North: South, South: North, East: West, West: East}

def handle_tile():
	till()
	plant(Entities.Cactus)
	while measure() != 0:
		harvest()
		plant(Entities.Cactus)

clear()
for _ in range(get_world_size()-1):
	for direction in MOVES:
		handle_tile()
		move(direction)
for direction in MOVES:
	handle_tile()
	use_item(Items.Water)
	move(direction)
# check last 3 tiles for cactus growth
REVERSED_MOVES = MOVES[::-1]
moves_len = len(REVERSED_MOVES)
move(OOP[direction])
while not can_harvest():
	pass
move(OOP[MOVES[::-1][0]])
while not can_harvest():
	pass
harvest()
