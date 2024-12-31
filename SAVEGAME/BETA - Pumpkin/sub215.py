MOVES = generate_moves()
move_x2, move_y2 = loadData(get_world_size())

clear()
for direction in MOVES:
	till()
	plant(Entities.Pumpkin)
	use_item(Items.Water)
	move(direction)

while num_items(Items.Pumpkin) < 100000:
	pumpkin_set = []
	# 1. just plant and move
	for direction in MOVES:
		plant(Entities.Pumpkin)
		move(direction)
	# 2. plant and append to dict
	for direction in MOVES:
		if not can_harvest():
			plant(Entities.Pumpkin)
			if get_water() < 0.2:
				use_item(Items.Water)
			pumpkin_set.append((get_pos_x(), get_pos_y()))
		move(direction)
	# 3. visit all missing pumpkins until ready to harvest
	while len(pumpkin_set) > num_items(Items.Fertilizer)/2:
		for pos in pumpkin_set:
			navi_to_pos(pos)
			if can_harvest():
				pumpkin_set.remove(pos)
			else:
				plant(Entities.Pumpkin)
	# 4. fertilize the remaining pumpkins
	for pos in pumpkin_set:
		navi_to_pos(pos)
		while not can_harvest():
			plant(Entities.Pumpkin)
			use_item(Items.Fertilizer)
	# 5. harvest
	harvest()
	