MOVES = generate_moves_light()
move_x, move_y = loadDataList(get_world_size())
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

	tpos = (get_pos_x(), get_pos_y())
	# 3. visit all missing pumpkins until ready to harvest
	while len(pumpkin_set) > num_items(Items.Fertilizer)/2+3:
		for pos in pumpkin_set:
			navi_to_list_pos(pos, tpos)
			tpos = pos
			if can_harvest():
				pumpkin_set.remove(pos)
			else:
				plant(Entities.Pumpkin)
	# 4. fertilize the remaining pumpkins
	for pos in pumpkin_set:
		navi_to_list_pos(pos, tpos)
		tpos = pos
		if get_water() < 0.75:
			use_item(Items.Water)
		while not can_harvest():
			plant(Entities.Pumpkin)
			use_item(Items.Fertilizer)
	# 5. harvest
	harvest()



pumpkin_set = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
ticks = get_tick_count()
pumpkin_set.remove((6, 0))
quick_print(get_tick_count() - ticks)
