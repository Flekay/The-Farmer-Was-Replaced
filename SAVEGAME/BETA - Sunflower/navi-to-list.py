def loadDataList(size=get_world_size()):
	def shift_list(l):
		return [l[-1]] + l[:-1]
	if size == 3:
		move_x = [
			[],
			[East],
			[West],
		]
		move_y = [
			[],
			[North],
			[South],
		]
	elif size == 4:
		move_x = [
			[],
			[East],
			[West, West],
			[West],
		]
		move_y = [
			[],
			[North],
			[South, South],
			[South],
		]
	elif size == 5:
		move_x = [
			[],
			[East],
			[East, East],
			[West, West],
			[West],
		]
		move_y = [
			[],
			[North],
			[North, North],
			[South, South],
			[South],
		]
	elif size == 6:
		move_x = [
			[],
			[East],
			[East, East],
			[West, West, West],
			[West, West],
			[West],
		]
		move_y = [
			[],
			[North],
			[North, North],
			[South, South, South],
			[South, South],
			[South],
		]
	elif size == 7:
		move_x = [
			[],
			[East],
			[East, East],
			[East, East, East],
			[West, West, West],
			[West, West],
			[West],
		]
		move_y = [
			[],
			[North],
			[North, North],
			[North, North, North],
			[South, South, South],
			[South, South],
			[South],
		]
	elif size == 8:
		move_x = [
			[],
			[East],
			[East, East],
			[East, East, East],
			[West, West, West, West],
			[West, West, West],
			[West, West],
			[West],
		]
		move_y = [
			[],
			[North],
			[North, North],
			[North, North, North],
			[South, South, South, South],
			[South, South, South],
			[South, South],
			[South],
		]
	elif size == 9:
		move_x = [
			[],
			[East],
			[East, East],
			[East, East, East],
			[East, East, East, East],
			[West, West, West, West],
			[West, West, West],
			[West, West],
			[West],
		]
		move_y = [
			[],
			[North],
			[North, North],
			[North, North, North],
			[North, North, North, North],
			[South, South, South, South],
			[South, South, South],
			[South, South],
			[South],
		]
	elif size == 10:
		move_x = [
			[],
			[East],
			[East, East],
			[East, East, East],
			[East, East, East, East],
			[West, West, West, West, West],
			[West, West, West, West],
			[West, West, West],
			[West, West],
			[West],
		]
		move_y = [
			[],
			[North],
			[North, North],
			[North, North, North],
			[North, North, North, North],
			[South, South, South, South, South],
			[South, South, South, South],
			[South, South, South],
			[South, South],
			[South],
		]

	# shift lists
	move_x_list = [move_x]
	move_y_list = [move_y]
	for _ in range(1, size):
		move_x_list.append(shift_list(move_x_list[-1]))
		move_y_list.append(shift_list(move_y_list[-1]))

	return move_x_list, move_y_list

def navi_to_list(goal_x, goal_y, start_x = get_pos_x(), start_y = get_pos_y()):
	for fx in move_data_x[start_x][goal_x]:
		move(fx)
	for fy in move_data_y[start_y][goal_y]:
		move(fy)


def navi_to_list_pos(goal_pos, start_pos = (get_pos_x(), get_pos_y())):
	goal_x, goal_y = goal_pos
	start_x, start_y = start_pos
	for fx in move_data_x[start_x][goal_x]:
		move(fx)
	for fy in move_data_y[start_y][goal_y]:
		move(fy)
