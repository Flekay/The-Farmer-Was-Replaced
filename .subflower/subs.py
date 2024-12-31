def generate_small_moves():
	moves = [East]
	right_moves = []
	for _ in range(8):
		right_moves.append(East)
	right_moves.append(North)
	left_moves = []
	for _ in range(8):
		left_moves.append(West)
	left_moves.append(North)
	for _ in range(4):
		moves += right_moves
		moves += left_moves
	moves += right_moves
	moves[-1] = East
	for _ in range(8):
		moves.append(South)
	return moves

move(North)
FULL_MOVES = generate_moves_light()
SMALL_MOVES = generate_small_moves()
move_data_x, move_data_y = loadDataList(get_world_size())
power = [[],[],[],[],[],[],[],[],[]]

for direction in FULL_MOVES:
	till()
	plant(Entities.Sunflower)
	if get_pos_y() == 0:
		while measure() != 7:
			harvest()
			plant(Entities.Sunflower)
	else:
		m = measure()
		power[15-m].append((get_pos_x(), get_pos_y()))
		if m > 13:
			use_item(Items.Water)
			# if m > 14:
			# 	use_item(Items.Water)
	move(direction)

x = 0
y = 1
for points in power:
	while points:
		tx = x
		ty = y
		pos = points.pop(0)
		x, y = pos
		navi_to_list(x,y,tx,ty)

		if len(points) < 4:
			while not can_harvest() and num_items(Items.Fertilizer) > 0:
				use_item(Items.Fertilizer)
		if can_harvest():
			harvest()
		else:
			points.append(pos)
navi_to_list(0,1,x,y)

for _ in range(28):
	x = 0
	y = 1
	# replant sunflowers
	for direction in SMALL_MOVES:
		plant(Entities.Sunflower)
		if measure() > 13 and get_water() < 0.7:
			use_item(Items.Water)
		power[15-measure()].append((get_pos_x(), get_pos_y()))
		move(direction)


	# harvest sunflowers highest petals to lowest
	for points in power:
		while points:
			tx = x
			ty = y
			pos = points.pop(0)
			x, y = pos
			navi_to_list(x,y,tx,ty)

			if len(points) < 4:
				while not can_harvest() and num_items(Items.Fertilizer) > 0:
					use_item(Items.Fertilizer)
			if can_harvest():
				harvest()
			else:
				points.append(pos)

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
			# navi_to_list_pos(points[0])
			# navi_to_list(x,y)
			for fx in move_data_x[tx][x]:
				move(fx)
			for fy in move_data_y[ty][y]:
				move(fy)

			if len(points) < 5:
				while not can_harvest() and num_items(Items.Fertilizer) > 0:
					use_item(Items.Fertilizer)
			if can_harvest():
				points.pop(0)
				harvest()
			else:
				points.append(points.pop(0))

	for fx in move_data_x[x][0]:
		move(fx)
	for fy in move_data_y[y][1]:
		move(fy)
