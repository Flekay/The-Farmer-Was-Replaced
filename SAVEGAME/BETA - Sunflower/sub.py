move(North)
FULL_MOVES = generate_moves_light()
SMALL_MOVES = generate_small_moves()
move_data_x, move_data_y = loadDataList(get_world_size())
power = [[],[],[],[],[],[],[],[],[]]
index = {15: 0, 14: 1, 13: 2, 12: 3, 11: 4, 10: 5, 9: 6, 8: 7, 7: 8}
i = 0
for direction in FULL_MOVES:
	till()
	plant(Entities.Sunflower)
	if get_pos_y() == 0:
		while measure() != 7:
			harvest()
			plant(Entities.Sunflower)
	else:
		m = measure()
		power[index[m]].append((get_pos_x(), get_pos_y()))
		if m > 13:
			use_item(Items.Water)
			if m > 14:
				use_item(Items.Water)
		i += 1
	move(direction)

x = 0
y = 1
for points in power:
	while points:
		tx = x
		ty = y
		x, y = points[0]
		navi_to_list(x,y,tx,ty)

		if can_harvest():
			points.pop(0)
			harvest()
		else:
			if len(points) < 4:
				skip = False
				while use_item(Items.Fertilizer):
					if can_harvest():
						points.pop(0)
						harvest()
						skip = True
						break
				if skip:
					continue
			points.append(points.pop(0))
navi_to_list(0,1,x,y)



for _ in range(28):
	x = 0
	y = 1
	# replant sunflowers
	for direction in SMALL_MOVES:
		plant(Entities.Sunflower)
		if measure() > 13 and get_water() < 0.7:
			use_item(Items.Water)
		power[index[measure()]].append((get_pos_x(), get_pos_y()))
		move(direction)


	# harvest sunflowers highest petals to lowest
	for points in power:
		while points:
			tx = x
			ty = y
			x, y = points[0]
			navi_to_list(x,y,tx,ty)

			if len(points) < 5:
				while not can_harvest() and num_items(Items.Fertilizer) > 0:
					use_item(Items.Fertilizer)
			if can_harvest():
				points.pop(0)
				harvest()
			else:
				points.append(points.pop(0))

	navi_to_list(0,1,x,y)


while num_items(Items.Power) < 100000:
	x = 0
	y = 1
	# replant sunflowers
	for direction in SMALL_MOVES:
		plant(Entities.Sunflower)
		if measure() > 13 and get_water() < 0.7:
			use_item(Items.Water)
		power[index[measure()]].append((get_pos_x(), get_pos_y()))
		move(direction)


	# harvest sunflowers highest petals to lowest
	for points in power:
		while points:
			tx = x
			ty = y
			x, y = points[0]
			navi_to_list(x,y,tx,ty)

			if len(points) < 6:
				while not can_harvest() and num_items(Items.Fertilizer) > 0:
					use_item(Items.Fertilizer)
			if can_harvest():
				points.pop(0)
				harvest()
			else:
				points.append(points.pop(0))

	navi_to_list(0,1,x,y)
	