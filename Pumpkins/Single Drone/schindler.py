MOVES = generate_moves()
move_x2, move_y2 = loadData(get_world_size())
pumpkin_set = []

clear()
for direction in MOVES:
	till()
	use_item(Items.Water)
	use_item(Items.Water)
	use_item(Items.Water)
	use_item(Items.Water)
	move(direction)



while True:
	# 1. just plant and move
	for direction in MOVES:
		plant(Entities.Pumpkin)
		if get_water() < 0.75:
			use_item(Items.Water)
		move(direction)
	# 2. plant and append to dict
	for direction in MOVES:
		if not can_harvest():
			plant(Entities.Pumpkin)
			pumpkin_set.append((get_pos_x(), get_pos_y()))
		move(direction)
	# 3. visit all missing pumpkins until ready to harvest
	while len(pumpkin_set) > 0:
		for pos in pumpkin_set:
			navi_to_pos(pos)
			if can_harvest():
				pumpkin_set.remove(pos)
			else:
				plant(Entities.Pumpkin)
	# 4. harvest
	harvest()
