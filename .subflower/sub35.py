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




clear()
move(North)
FULL_MOVES = generate_moves()
SMALL_MOVES = generate_small_moves() # only on 10x10 grid for testing
move_data_x, move_data_y = loadDataList(get_world_size()) # can be replaced with navi-to-pos.py for better performance
power = [[],[],[],[],[],[],[],[],[]]
index = {15: 0, 14: 1, 13: 2, 12: 3, 11: 4, 10: 5, 9: 6, 8: 7, 7: 8}

for direction in FULL_MOVES:
	till()
	plant(Entities.Sunflower)
	if get_pos_y() == 0:
		while measure() != 7:
			harvest()
			plant(Entities.Sunflower)
	move(direction)



while num_items(Items.Power) < 100000:
	# replant sunflowers
	for direction in SMALL_MOVES:
		plant(Entities.Sunflower)
		if measure() > 13:
			if get_water() < 0.75:
				use_item(Items.Water)
		power[index[measure()]].append((get_pos_x(), get_pos_y()))
		move(direction)


	# harvest sunflowers highest petals to lowest
	for points in power:
		while points:
			navi_to_list_pos(points[0])
			if len(points) < 4:
				while not can_harvest() and num_items(Items.Fertilizer) > 0:
					use_item(Items.Fertilizer)
			if can_harvest():
				points.pop(0)
				harvest()
			else:
				points.append(points.pop(0))
	for fx in move_data_x[get_pos_x()][0]:
		move(fx)
	for fy in move_data_y[get_pos_y()][1]:
		move(fy)
		