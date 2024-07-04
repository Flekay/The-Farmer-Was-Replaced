MOVES = generate_moves()
move_x2, move_y2 = loadData(get_world_size())
PUMPKIN = Entities.Pumpkin
FERTILIZER = Items.Fertilizer
WATER = Items.Water_Tank
pumpkin_set = []

clear()
for direction in MOVES:
	till()
	move(direction)



for i in range(0, 1, 0):
	# 1. just plant and move
	for direction in MOVES:
		plant(PUMPKIN)
		if get_water() < 0.75:
			use_item(WATER)
		move(direction)
	# 2. plant and append to dict
	for direction in MOVES:
		if not can_harvest():
			plant(PUMPKIN)
			pumpkin_set.append((get_pos_x(), get_pos_y()))
		move(direction)
	# 3. visit all missing pumpkins until ready to harvest
	while len(pumpkin_set) > 0:
		for pos in pumpkin_set:
			navi_to_pos(pos)
			if can_harvest():
				pumpkin_set.remove(pos)
			else:
				plant(PUMPKIN)
	# 4. harvest
	harvest()