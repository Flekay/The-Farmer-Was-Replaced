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
	if get_pos_y() == 0:
		plant(Entities.Sunflower)
		while measure() != 7:
			harvest()
			plant(Entities.Sunflower)
	move(direction)

def power_skip(ws = get_world_size()):

	# pre water
	for direction in SMALL_MOVES:
		while get_water() != 1:
			use_item(Items.Water)
		move(direction)

	for _ in range(9): # ~1min
		current_x = 0
		current_y = 1
		# replant sunflowers
		for direction in SMALL_MOVES:
			plant(Entities.Sunflower)
			power[index[measure()]].append((get_pos_x(), get_pos_y()))
			move(direction)


		# harvest sunflowers highest petals to lowest
		for points in power:
			while points:

		# sub optimal pathing 3.47k / min
		# 		navi_to_list_pos(points.pop(0))
		# 		while not can_harvest():
		# 			use_item(Items.Fertilizer)
		# 		harvest()
		# for fx in move_data_x[get_pos_x()][0]:
		# 	move(fx)
		# for fy in move_data_y[get_pos_y()][1]:
		# 	move(fy)

		# optimal pathing 3.64k / min
				nearest_dist = 999
				for point in points:
					x, y = point
					dx = abs(current_x - x)
					dy = abs(current_y - y)
					dist = min(dx, ws - dx) + min(dy, ws - dy)
					if dist < nearest_dist:
						nearest = point
						nearest_dist = dist

				for fx in move_data_x[current_x][nearest[0]]:
					move(fx)
				for fy in move_data_y[current_y][nearest[1]]:
					move(fy)
				while not can_harvest():
					use_item(Items.Fertilizer)
				harvest()
				current_x, current_y = nearest
				points.remove(nearest)
		for fx in move_data_x[current_x][0]:
			move(fx)
		for fy in move_data_y[current_y][1]:
			move(fy)

while True:
	power_skip()
