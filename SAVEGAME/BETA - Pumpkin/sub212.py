MOVES = generate_moves()
move_data_x, move_data_y = loadDataList(get_world_size())
pumpkin_set = []

# 0. Preplant
for direction in MOVES:
	till()
	plant(Entities.Pumpkin)
	use_item(Items.Water)
	move(direction)

# 21 * 5000
for _ in range(21):
	pumpkin_set = []
	# 1. just plant and move
	for direction in MOVES:
		plant(Entities.Pumpkin)
		move(direction)
	# 1.5 just plant and move
	for direction in MOVES:
		plant(Entities.Pumpkin)
		move(direction)
	# 2. plant and append to dict
	for direction in MOVES:
		if not can_harvest():
			plant(Entities.Pumpkin)
			if get_water() < 0.75:
				use_item(Items.Water)
			#use_item(Items.Water)
			pumpkin_set.append((get_pos_x(), get_pos_y()))
		move(direction)
	# 3. visit all missing pumpkins until ready to harvest
	while len(pumpkin_set) > num_items(Items.Fertilizer)/2:
		for pos in pumpkin_set:
			navi_to_list_pos(pos)
			if can_harvest():
				pumpkin_set.remove(pos)
			else:
				plant(Entities.Pumpkin)
	# 4. fertilize the remaining pumpkins
	for pos in pumpkin_set:
		navi_to_list_pos(pos)
		while not can_harvest():
			plant(Entities.Pumpkin)
			use_item(Items.Fertilizer)
	# 5. harvest
	harvest()
	